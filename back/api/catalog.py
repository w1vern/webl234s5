
from fastapi import Cookie, Depends, HTTPException, Response
from fastapi_controllers import Controller, get, post
import redis
from sqlalchemy.ext.asyncio import AsyncSession

from back.authorize_user import authorize_user
from back.config import Config
from back.schemes.basket import Basket
from database.database import session_manager
from database.models.user import User
from database.redis import RedisDB, get_redis_client
from database.repositories.product_repository import ProductRepository
from database.repositories.user_repository import UserRepository


class CatalogController(Controller):
	prefix = '/catalog'
	tags = ['catalog']

	def __init__(self, session: AsyncSession = Depends(session_manager.session)) -> None:
		self.session = session

	@get("/")
	async def get_cards(self, redis: redis.Redis = Depends(get_redis_client)):
		pr = ProductRepository(self.session)
		products = await pr.get_all()
		free_workers = int(await redis.get(f"{RedisDB.free_workers}"))
		return list([{"id": product.id, "label": product.label, "description": product.description, "price": product.price, "sale": product.sale, "path_to_image": product.path_to_image, "time_to_resolve": product.time_to_resolve, "can_be_ordered": free_workers // product.worker_count } for product in products])

	@post("/new_basket_state") #not optimal but interesting
	async def new_basket_state(self, basket: Basket, redis: redis.Redis = Depends(get_redis_client), user: User = Depends(authorize_user)):
		for product in basket.products:
			if not product.count > 0:
				basket.products.remove(product)
		redis.set(f"{RedisDB.basket}:{user.id}", basket.model_dump_json())
		pr = ProductRepository(self.session)
		products = await pr.get_all()
		products_dict = dict()
		for product in products:
			products_dict[product.id] = product.worker_count
		prefix = f"{RedisDB.basket}:*"
		keys = list(redis.scan_iter(match=prefix))
		baskets = await redis.mget(keys)
		locked_workers = 0
		for b in baskets:
			basket_products = Basket.model_validate_json(b)
			for product in basket_products.products:
				locked_workers += products_dict[product.id]*product.count
		redis.set(f"{RedisDB.free_workers}", Config.worker_count - locked_workers) 
		return {"message": "OK"}

	@get("/basket")
	async def get_basket(self, redis: redis.Redis = Depends(get_redis_client), user: User = Depends(authorize_user)):
		byte_basket = await redis.get(f"{RedisDB.basket}:{user.id}")
		if byte_basket is None:
			return Basket(products=[])
		return Basket.model_validate_json(byte_basket)






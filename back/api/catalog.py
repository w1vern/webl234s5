
import json
from math import prod
from fastapi import Cookie, Depends, HTTPException, Response
from fastapi_controllers import Controller, get, post
import redis
from sqlalchemy.ext.asyncio import AsyncSession

from back.config import Config
from back.schemes.basket import Basket
from database.database import get_db_session
from database.redis import RedisDB, get_redis_client
from database.repositories.product_repository import ProductRepository
from database.repositories.user_repository import UserRepository




class CatalogController(Controller):
	prefix = '/catalog'
	tags = ['catalog']

	def __init__(self, session: AsyncSession = Depends(get_db_session)):
		self.session = session

	@get("/")
	async def get_cards(self, redis: redis.Redis = Depends(get_redis_client)):
		pr = ProductRepository(self.session)
		products = await pr.get_all()
		free_workers = int(redis.get(f"{RedisDB.free_workers}").decode('utf-8'))
		return list([{"id": product.id, "label": product.label, "description": product.description, "price": product.price, "path_to_image": product.path_to_image, "can_be_ordered": free_workers // product.worker_count } for product in products])

	@post("/new_basket_state")
	async def new_basket_state(self, basket: Basket, session_id : str = Cookie(default=None), redis: redis.Redis = Depends(get_redis_client)):
		if session_id is None:
			raise HTTPException(status_code=401, detail="Unauthorized")
		user_id = redis.get(f"{RedisDB.auth_session}:{session_id}")
		if user_id is None:
			raise HTTPException(status_code=401, detail="Unauthorized")
		user_id = user_id.decode('utf-8')
		ur = UserRepository(self.session)
		user = await ur.get_by_id(user_id)
		if user is None:
			raise HTTPException(status_code=401, detail="Unauthorized")
		redis.set(f"{RedisDB.basket}:{user_id}", basket.model_dump_json(), ex=Config.basket_lifetime)
		pr = ProductRepository(self.session)
		products = await pr.get_all()
		products_dict = dict()
		for product in products:
			products_dict[product.id] = product.worker_count
		prefix = f"{RedisDB.basket}:*"
		keys = list(redis.scan_iter(match=prefix))
		baskets = redis.mget(keys)
		locked_workers = 0
		for b in baskets:
			basket_products = Basket.model_validate_json(b.decode('utf-8'))
			for product in basket_products.products:
				locked_workers += products_dict[product.id]*product.count
				print(locked_workers)
		redis.set(f"{RedisDB.free_workers}", Config.worker_count - locked_workers) 
		return {"message": "OK"}



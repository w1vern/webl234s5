from datetime import UTC, datetime, timedelta
from itertools import product
import json
from fastapi import Cookie, Depends, HTTPException, Response
from fastapi_controllers import Controller, get, post
import redis
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.redis import RedisDB, get_redis_client
from database.repositories.product_repository import ProductRepository
from database.repositories.user_repository import UserRepository
from back.schemes.auth import LoginData, RegisterData




class CatalogController(Controller):
    prefix = '/catalog'
    tags = ['catalog']

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    @get("/")
    async def get_cards(self):
        pr = ProductRepository(self.session)
        products = await pr.get_all()
        return list([{"label": product.label, "description": product.description, "price": product.price, "path_to_image": product.path_to_image} for product in products])
    
    @post("/new_basket_state")
    async def new_basket_state(self, session_id : str = Cookie(default=None), redis: redis.Redis = Depends(get_redis_client)):
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
        pass
        return {"message": "OK"}
        
        
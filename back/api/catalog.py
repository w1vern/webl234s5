from datetime import UTC, datetime, timedelta
from itertools import product
import json
from fastapi import Cookie, Depends, HTTPException, Response
from fastapi_controllers import Controller, get, post
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
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
        
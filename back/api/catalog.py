from datetime import UTC, datetime, timedelta
from fastapi import Cookie, Depends, HTTPException, Response
from fastapi_controllers import Controller, get, post
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.repositories.user_repository import UserRepository
from back.schemes.auth import LoginData, RegisterData
from back.config import catalog




class CatalogController(Controller):
    prefix = '/catalog'
    tags = ['catalog']

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    @get("/")
    async def get_cards(self):
        return catalog
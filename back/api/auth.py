
from datetime import UTC, datetime, timedelta
import secrets
from fastapi import Cookie, Depends, HTTPException, Response
from fastapi_controllers import Controller, get, post
from sqlalchemy.ext.asyncio import AsyncSession

import redis
from database.database import get_db_session
from database.redis import get_redis_client
from database.repositories.user_repository import UserRepository
from back.config import Config, RedisDB
from back.schemes.auth import LoginData, RegisterData


class AuthController(Controller):
    prefix = '/auth'
    tags = ['auth']

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    @post("/login")
    async def login(self, response: Response, login_data: LoginData, redis: redis.Redis = Depends(get_redis_client)):
        ur = UserRepository(self.session)
        user = await ur.get_by_auth(login_data.phone, login_data.password)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        session_id = secrets.token_urlsafe()
        response.set_cookie(key='session_id', value=session_id,
                            max_age=Config.auth_session_lifetime, httponly=True)
        redis.set(f"{RedisDB.auth_session}:{session_id}", user.id, ex=Config.auth_session_lifetime)
        return {"message": "OK"}

    @post("/register")
    async def register(self, register_data: RegisterData):
        ur = UserRepository(self.session)
        if register_data.password != register_data.password_repeat:
            raise HTTPException(
                status_code=401, detail="passwords do not match")
        if not ur.get_by_phone(register_data.phone) is None:
            raise HTTPException(
                status_code=401, detail="user with this phone already exists")
        user = await ur.create(register_data.phone, register_data.password)
        self.session.commit()
        if user is None:
            raise HTTPException(
                status_code=401, detail="undefined error, try again")
        return {"message": "OK"}

    @post("/logout")
    async def logout(self, response: Response, redis: redis.Redis = Depends(get_redis_client), session_id: str = Cookie(default=None)):
        response.set_cookie(key='session', value='', max_age=0, httponly=True)
        redis.delete(f"{RedisDB.auth_session}:{session_id}")
        return {"message": "OK"}

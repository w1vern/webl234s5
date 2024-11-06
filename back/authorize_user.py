

from fastapi import Cookie, Depends, HTTPException
import redis
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models.user import User
from database.redis import RedisDB, get_redis_client
from database.repositories.user_repository import UserRepository


async def authorize_user(session_id: str = Cookie(default=None), redis: redis.Redis = Depends(get_redis_client), session: AsyncSession = Depends(get_db_session)) -> User:
    if session_id is None:
        raise HTTPException(status_code=401, detail="Сессия не существует или истекла")
    user_id = redis.get(f"{RedisDB.auth_session}:{session_id}")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Не удалось найти пользователя")
    user_id = user_id.decode('utf-8')
    ur = UserRepository(session)
    user = await ur.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="Пользователь не существует")
    return user
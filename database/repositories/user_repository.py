import secrets
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import check_password_hash, generate_password_hash

from database.models import *


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, phone_number: str, password: str) -> Optional[User]:
        user = User(phone_number=phone_number,
                    hashed_password=generate_password_hash(password))
        self.session.add(user)
        await self.session.flush()
        return await self.get_by_id(user.id)

    async def get_by_id(self, id: UUID) -> Optional[User]:
        stmt = select(User).where(User.id == id).limit(1)
        return await self.session.scalar(stmt)

    async def get_by_phone(self, phone_number: str) -> Optional[User]:
        stmt = select(User).where(User.phone_number == phone_number).limit(1)
        return await self.session.scalar(stmt)

    async def get_by_auth(self, phone_number: str, password: str) -> Optional[User]:
        stmt = select(User).where(User.phone_number == phone_number).limit(1)
        user: User = await self.session.scalar(stmt)
        if user is None:
            return None
        if not check_password_hash(user.hashed_password, password):
            return None
        return user

    async def update_secret(self, user: User) -> None:
        user.secret = secrets.token_urlsafe()
        await self.session.flush()

from pickletools import pynone
import secrets
from sqlalchemy.orm import Session
from sqlalchemy import false, select
from uuid import UUID
from database.models import *
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def create(self, phone_number: str, password: str, secret: str = secrets.token_urlsafe()) -> Optional[User]:
        user = User(phone_number=phone_number,
                    hashed_password=generate_password_hash(password), secret=secret)
        self.session.add(user)
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

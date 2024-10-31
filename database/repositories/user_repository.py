from pickletools import pynone
import secrets
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID
from database.models import *
from typing import Optional


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def get_by_id(self, id: UUID) -> Optional[User]:
        stmt = select(User).where(User.id == id).limit(1)
        return await self.session.scalar(stmt)
    
    async def create(self, phone_number: str, hashed_password: str, secret: str = secrets.token_urlsafe()) -> None:
        self.session.add(User(phone_number=phone_number, hashed_password=hashed_password, secret=secret))
        self.session.flush()

    async def get_by_phone(self, phone_number: str) -> Optional[User]:
        stmt = select(User).where(User.phone_number==phone_number).limit(1)
        return await self.session.scalar(stmt)
    
    async def update_secret(self, user: User) -> None:
        user.secret = secrets.token_urlsafe()
        self.session.flush()

    
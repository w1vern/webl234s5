from pickletools import pynone
import secrets
from sqlalchemy.orm import Session
from sqlalchemy import false, select
from uuid import UUID
from database.models import *
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash

from database.models.feedback import Feedback


class FeedbackRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def create(self, name: str, email: str, message: str) -> Optional[Feedback]:
        feedback = Feedback(name=name, email=email, message=message)
        self.session.add(feedback)
        await self.session.flush()
        return await self.get_by_id(feedback.id)
    
    async def get_by_id(self, id: UUID) -> Optional[Feedback]:
        stmt = select(Feedback).where(Feedback.id == id).limit(1)
        return await self.session.scalar(stmt)
    
    async def get_all(self) -> list[Feedback]:
        stmt = select(Feedback)
        return await self.session.scalars(stmt)
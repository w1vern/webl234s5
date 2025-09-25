
from typing import Optional
from uuid import UUID

from sqlalchemy import false, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import *
from database.models.feedback import Feedback


class FeedbackRepository:
    def __init__(self, session: AsyncSession) -> None:
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
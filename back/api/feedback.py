
from fastapi import Depends
from fastapi_controllers import Controller, post
from sqlalchemy.ext.asyncio import AsyncSession

from back.schemes.feedback import FeedbackData
from database.database import session_manager
from database.repositories.feedback_repository import FeedbackRepository


class FeedbackController(Controller):
    prefix = '/feedback'
    tags = ['feedback']

    def __init__(self, session: AsyncSession = Depends(session_manager.session)) -> None:
        self.session = session

    @post("/")
    async def add_feedback(self, feedback: FeedbackData) -> dict[str, str]:
        fr = FeedbackRepository(self.session)
        print(feedback.name)
        await fr.create(name=feedback.name, email=feedback.email, message=feedback.message)
        await self.session.commit()
        return {"message": "OK"}

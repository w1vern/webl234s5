from datetime import UTC, datetime, timedelta
from itertools import product
import json
from fastapi import Cookie, Depends, HTTPException, Response
from fastapi_controllers import Controller, get, post
from sqlalchemy.ext.asyncio import AsyncSession

from back.schemes.feedback import FeedbackData
from database.database import session_manager
from database.models.feedback import Feedback
from database.repositories.feedback_repository import FeedbackRepository
from database.repositories.product_repository import ProductRepository
from database.repositories.user_repository import UserRepository
from back.schemes.auth import LoginData, RegisterData


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

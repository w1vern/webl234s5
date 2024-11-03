

from pydantic import BaseModel


class FeedbackData(BaseModel):
    name: str
    email: str
    message: str

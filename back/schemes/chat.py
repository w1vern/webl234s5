
from uuid import UUID

from pydantic import BaseModel


class Message(BaseModel):
    text: str
    from_user: bool

class Chat(BaseModel):
    id: UUID
    name: str


from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.chat import Chat
from database.models.message import Message


class MessageRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, text: str, chat: Chat, from_user: bool) -> Message:
        message = Message(text=text, chat_id=chat.id)
        self.session.add(message)
        await self.session.flush()
        message = await self.get_by_id(message.id)
        if message is None:
            raise Exception("Message was not created")
        return message

    async def get_by_id(self, id: UUID) -> Message | None:
        stmt = select(Message).where(Message.id == id).limit(1)
        return await self.session.scalar(stmt)

    async def get_all(self) -> list[Message]:
        stmt = select(Message)
        return list(await self.session.scalars(stmt))

    async def get_by_chat(self, chat: Chat) -> list[Message]:
        stmt = select(Message).where(Message.chat_id == chat.id).order_by(Message.timestamp)
        return list(await self.session.scalars(stmt))

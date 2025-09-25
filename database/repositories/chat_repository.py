
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.chat import Chat
from database.models.user import User


class ChatRepository:
	def __init__(self, session: AsyncSession) -> None:
		self.session = session

	async def create(self, name: str, user: User) -> Chat:
		chat = Chat(name=name, user_id=user.id)
		self.session.add(chat)
		await self.session.flush()
		chat = await self.get_by_id(chat.id)
		if chat is None:
			raise Exception("Chat was not created")
		return chat
	
	async def get_by_id(self, id: UUID) -> Chat | None:
		stmt = select(Chat).where(Chat.id == id).limit(1)
		return await self.session.scalar(stmt)
	
	async def get_all(self) -> list[Chat]:
		stmt = select(Chat)
		return list(await self.session.scalars(stmt))
	
	async def get_by_user(self, user: User) -> list[Chat]:
		stmt = select(Chat).where(Chat.user_id == user.id).order_by(Chat.timestamp)
		return list(await self.session.scalars(stmt))


from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database.models.base import Base
from database.models.chat import Chat


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    text: Mapped[str] = mapped_column()
    chat_id: Mapped[UUID] = mapped_column(ForeignKey("chats.id"))
    from_user: Mapped[bool] = mapped_column(nullable=True)
    timestamp: Mapped[datetime] = mapped_column(server_default=func.now())

    chat: Mapped[Chat] = relationship(lazy="selectin", foreign_keys=[chat_id])

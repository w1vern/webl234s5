import uuid
from uuid import uuid4

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    phone_number: Mapped[str] = mapped_column(unique=True)
    hashed_password:Mapped[str] = mapped_column()
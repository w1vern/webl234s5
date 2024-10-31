from sqlalchemy.orm import mapped_column, Mapped, relationship
from database.models.base import Base
from uuid import uuid4
import uuid



class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    phone_number: Mapped[str] = mapped_column(unique=True)
    hashed_password:Mapped[str] = mapped_column()
    secret: Mapped[str] = mapped_column()
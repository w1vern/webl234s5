from sqlalchemy.orm import mapped_column, Mapped
from database.models.base import Base
from uuid import uuid4
import uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    label: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[str] = mapped_column()
    path_to_image: Mapped[str] = mapped_column()
     
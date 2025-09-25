import datetime
import uuid
from uuid import uuid4

from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    message: Mapped[str] = mapped_column()
     
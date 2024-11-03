import datetime
from sqlalchemy.orm import mapped_column, Mapped
from database.models.base import Base
from uuid import uuid4
import uuid
class Feedback(Base):
    __tablename__ = "feedbacks"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    message: Mapped[str] = mapped_column()
     
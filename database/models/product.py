import datetime
from sqlalchemy.orm import mapped_column, Mapped
from database.models.base import Base
from uuid import uuid4
import uuid
class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    label: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    sale: Mapped[float] = mapped_column()
    path_to_image: Mapped[str] = mapped_column()
    worker_count : Mapped[int] = mapped_column()
    time_to_resolve: Mapped[datetime.timedelta] = mapped_column()
     
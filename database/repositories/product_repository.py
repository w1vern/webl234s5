import datetime
from pickletools import pynone
import secrets
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID
from database.models import *
from typing import Optional


class ProductRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def get_by_id(self, id: UUID) -> Optional[Product]:
        stmt = select(Product).where(Product.id == id).limit(1)
        return await self.session.scalar(stmt)
    
    async def create(self, label: str, description: str, price: str, path_to_image: str, worker_count: int = 1, time_to_resolve: datetime.timedelta = datetime.timedelta(days=1)) -> None:
        self.session.add(Product(label=label, description=description, price=price, path_to_image=path_to_image, worker_count=worker_count, time_to_resolve=time_to_resolve))
        await self.session.flush()

    async def get_all(self) -> list[Product]:
        stmt = select(Product)
        return await self.session.scalars(stmt)

    
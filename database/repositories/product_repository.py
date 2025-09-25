import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import *


class ProductRepository:
	def __init__(self, session: AsyncSession) -> None:
		self.session = session

	async def create(self, label: str, description: str, price: float, sale: float, path_to_image: str, worker_count: int = 1, time_to_resolve: datetime.timedelta = datetime.timedelta(days=1)) -> Optional[Product]:
		product = Product(label=label, description=description, price=price, sale=sale,
			path_to_image=path_to_image, worker_count=worker_count, time_to_resolve=time_to_resolve)
		self.session.add(product)
		await self.session.flush()
		return await self.get_by_id(product.id)

	async def get_by_id(self, id: UUID) -> Optional[Product]:
		stmt = select(Product).where(Product.id == id).limit(1)
		return await self.session.scalar(stmt)

	async def get_all(self) -> list[Product]:
		stmt = select(Product)
		return await self.session.scalars(stmt)

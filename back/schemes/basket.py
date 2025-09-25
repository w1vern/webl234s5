

import uuid

from pydantic import BaseModel


class Product(BaseModel):
    id: uuid.UUID
    count: int

class Basket(BaseModel):
    products: list[Product]
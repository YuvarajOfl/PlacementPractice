from pydantic import BaseModel
from typing import List

class ItemCreate(BaseModel):
    product_name: str
    quantity: int
    price: float


class BillCreate(BaseModel):
    customer_name: str
    items: List[ItemCreate]


class ItemOut(BaseModel):
    product_name: str
    quantity: int
    price: float

    class Config:
        from_attributes = True


class BillOut(BaseModel):
    id: int
    customer_name: str
    total_amount: float
    items: List[ItemOut]

    class Config:
        from_attributes = True
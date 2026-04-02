from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    total_amount = Column(Float)

    items = relationship("BillItem", back_populates="bill")


class BillItem(Base):
    __tablename__ = "bill_items"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100))
    quantity = Column(Integer)
    price = Column(Float)

    bill_id = Column(Integer, ForeignKey("bills.id"))

    bill = relationship("Bill", back_populates="items")
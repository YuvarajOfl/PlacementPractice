from sqlalchemy import Column, Integer, String
from app.database import Base

class Donor(Base):
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    blood_group = Column(String(10))
    location = Column(String(100))
    phone = Column(String(15))
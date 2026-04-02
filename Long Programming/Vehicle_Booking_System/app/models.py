from sqlalchemy import Column, Integer, String
from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100))
    pickup = Column(String(100))
    drop_location = Column(String(100))
    vehicle_type = Column(String(50))
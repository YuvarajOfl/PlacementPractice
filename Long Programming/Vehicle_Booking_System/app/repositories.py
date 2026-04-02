from app.models import Booking
from app.database import SessionLocal

def create_booking(data):
    db = SessionLocal()
    try:
        booking = Booking(
            user_name=data.user_name,
            pickup=data.pickup,
            drop_location=data.drop_location,
            vehicle_type=data.vehicle_type
        )
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking
    finally:
        db.close()

def get_all_bookings():
    db = SessionLocal()
    try:
        return db.query(Booking).all()
    finally:
        db.close()
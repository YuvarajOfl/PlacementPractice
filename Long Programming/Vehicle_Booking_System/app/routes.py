from fastapi import APIRouter
from app.schema import BookingRequest
from app.services import book_ride, fetch_all_bookings

router = APIRouter()

@router.get("/bookings")
def get_bookings():
    return fetch_all_bookings()

@router.post("/book-ride")
def book_ride_api(request: BookingRequest):
    return book_ride(request)
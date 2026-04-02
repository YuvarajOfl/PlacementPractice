from app.repositories import create_booking, get_all_bookings

def book_ride(request):
    
    if request.pickup == request.drop_location:
        return {"message": "Pickup and Drop cannot be same"}

    booking = create_booking(request)

    return {
        "message": f"Ride booked successfully for {booking.user_name}"
    }

def fetch_all_bookings():
    bookings = get_all_bookings()

    return bookings
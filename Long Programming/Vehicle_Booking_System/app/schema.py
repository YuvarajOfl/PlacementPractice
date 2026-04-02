from pydantic import BaseModel

class BookingRequest(BaseModel):
    user_name: str
    pickup: str
    drop_location: str
    vehicle_type: str

class BookingResponse(BaseModel):
    message: str
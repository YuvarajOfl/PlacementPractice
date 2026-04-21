from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    email: str
    meter_number: str


class BillCreate(BaseModel):
    customer_id: int
    units_consumed: float
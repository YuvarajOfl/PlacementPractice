from pydantic import BaseModel

class DonorCreate(BaseModel):
    name: str
    blood_group: str
    location: str
    phone: str

class DonorOut(BaseModel):
    id: int
    name: str
    blood_group: str
    location: str
    phone: str

    class Config:
        orm_mode = True
from fastapi import APIRouter
from app.schema import BillCreate, BillOut
from app.services import generate_bill, fetch_bills
from typing import List

router = APIRouter()

@router.post("/bill", response_model=BillOut)
def create_bill_api(request: BillCreate):
    return generate_bill(request)

@router.get("/bills", response_model=List[BillOut])
def get_bills():
    return fetch_bills()

@router.get("/")
def home():
    return {"message": "Supermarket Billing API running"}
from fastapi import APIRouter
from typing import List
from app.donor_schema import DonorCreate, DonorOut
from app.donor_service import add_donor, fetch_donors

router = APIRouter()

@router.post("/donor")
def add_donor_api(request: DonorCreate):
    return add_donor(request)


@router.get("/donors", response_model=List[DonorOut])
def fetch_donors_api():
    return fetch_donors()
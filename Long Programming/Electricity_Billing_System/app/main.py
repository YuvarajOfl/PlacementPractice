from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/customers/")
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        meter_number=customer.meter_number
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def calculate_bill(units):
    if units <= 100:
        return units * 2
    elif units <= 300:
        return (100 * 2) + (units - 100) * 3
    else:
        return (100 * 2) + (200 * 3) + (units - 300) * 5

@app.get("/customers/")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(models.Customer).all()
    return customers

@app.get("/customers/{customer_id}/bills")
def get_customer_bills(customer_id: int, db: Session = Depends(get_db)):
    bills = db.query(models.Bill).filter(models.Bill.customer_id == customer_id).all()

    if not bills:
        raise HTTPException(status_code=404, detail="No bills found for this customer")

    return bills

@app.post("/generate-bill/")
def generate_bill(bill: schemas.BillCreate, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == bill.customer_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    amount = calculate_bill(bill.units_consumed)

    new_bill = models.Bill(
        customer_id=bill.customer_id,
        units_consumed=bill.units_consumed,
        amount=amount
    )

    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)

    return {
        "customer": customer.name,
        "units": bill.units_consumed,
        "amount": amount
    }

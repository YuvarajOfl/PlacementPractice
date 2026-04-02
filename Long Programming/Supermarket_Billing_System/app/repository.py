from app.database import SessionLocal
from app.models import Bill, BillItem
from sqlalchemy.orm import joinedload

def create_bill(data):
    db = SessionLocal()
    try:
        total = 0

        bill = Bill(customer_name=data.customer_name, total_amount=0)
        db.add(bill)
        db.commit()
        db.refresh(bill)

        for item in data.items:
            total += item.quantity * item.price

            db_item = BillItem(
                product_name=item.product_name,
                quantity=item.quantity,
                price=item.price,
                bill_id=bill.id
            )
            db.add(db_item)

        bill.total_amount = total
        db.commit()
        db.refresh(bill)

        return bill
    finally:
        db.close()

def get_all_bills():
    db = SessionLocal()
    try:
        return db.query(Bill).options(joinedload(Bill.items)).all()
    finally:
        db.close()
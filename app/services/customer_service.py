from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.customer_model import Customer
from app.schemas.customer_schema import CustomerCreate

def create_customer(db: Session, dto: CustomerCreate):
    if db.query(Customer).filter(Customer.phone == dto.phone).first():
        raise HTTPException(status_code=400, detail="이미 등록된 전화번호입니다")

    customer = Customer(name=dto.name, phone=dto.phone)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
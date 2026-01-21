from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.schemas.customer_schema import CustomerCreate, CustomerResponse
from app.services.customer_service import create_customer

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("", response_model=CustomerResponse)
def create(dto: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, dto)
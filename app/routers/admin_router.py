from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from app.services.admin_service import AdminService
from app.schemas.admin_schema import AdminCreate, AdminResponse
from app.core.response import success

router = APIRouter(prefix="/admins", tags=["Admins"])


@router.post("", response_model=AdminResponse)
def create_admin(dto: AdminCreate, db: Session = Depends(get_db)):
    service = AdminService(db)
    admin = service.create(dto.dict())
    return success(admin)
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.deps import get_db
from app.services.admin_service import AdminService
from app.schemas.admin_schema import AdminCreate, AdminUpdate, AdminResponse
from app.schemas.common import ApiResponse, PageResponse
from app.core.response import success

router = APIRouter(prefix="/admins", tags=["Admins"])


@router.post("", response_model=AdminResponse)
def create_admin(dto: AdminCreate, db: Session = Depends(get_db)):
    service = AdminService(db)
    admin = service.create(dto.dict())
    return success(admin)


@router.get("/{admin_id}", response_model=ApiResponse[AdminResponse])
def get_admin(admin_id: int, db: Session = Depends(get_db)):
    service = AdminService(db)
    return success(service.get(admin_id))


@router.get("", response_model=ApiResponse[PageResponse[AdminResponse]])
def get_all_admin(
    page: int = Query(1, ge=1),
    size: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    service = AdminService(db)
    return success(service.paginate(page, size))


@router.put("/{admin_id}", response_model=ApiResponse[AdminResponse])
def update_admin(
    admin_id: int,
    dto: AdminUpdate,
    db: Session = Depends(get_db)
):
    service = AdminService(db)
    return success(service.update(admin_id, dto.dict(exclude_unset=True)))


@router.delete("/{admin_id}", response_model=ApiResponse[None])
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    service = AdminService(db)
    service.delete(admin_id)
    return success(None, message="삭제 완료")
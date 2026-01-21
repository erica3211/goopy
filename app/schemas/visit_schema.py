from pydantic import BaseModel
from app.core.enums import VisitStatus

class VisitCreate(BaseModel):
    customer_id: int
    estimated_minutes: int = 15

class VisitResponse(BaseModel):
    id: int
    customer_id: int
    status: VisitStatus
    queue_order: int
    estimated_minutes: int

    class Config:
        from_attributes = True
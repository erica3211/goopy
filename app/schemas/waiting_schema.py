from pydantic import BaseModel
from app.core.enums import WaitingStatus

class WaitingCreate(BaseModel):
    customer_id: int
    estimated_minutes: int = 15

class WaitingUpdate(BaseModel):
    customer_id: int
    estimated_minutes: int = 15
    
class WaitingResponse(BaseModel):
    id: int
    customer_id: int
    status: WaitingStatus
    queue_order: int
    estimated_minutes: int

    class Config:
        from_attributes = True
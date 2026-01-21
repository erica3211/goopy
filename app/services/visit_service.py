from sqlalchemy.orm import Session
from app.models.visit_model import Visit
from app.core.enums import VisitStatus
from app.schemas.visit_schema import VisitCreate

def create_visit(db: Session, dto: VisitCreate):
    queue_order = db.query(Visit).count() + 1

    visit = Visit(
        customer_id=dto.customer_id,
        status=VisitStatus.WAITING,
        queue_order=queue_order,
        estimated_minutes=dto.estimated_minutes
    )
    db.add(visit)
    db.commit()
    db.refresh(visit)
    return visit
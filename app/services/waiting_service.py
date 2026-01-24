from app.core.pagination import paginate
from app.schemas.waiting_schema import WaitingResponse
from app.services.base_service import BaseService
from app.models.waiting_model import Waiting
from app.models.customer_model import Customer
from app.core.enums import WaitingStatus

class WaitingService(BaseService):
    model = Waiting

    # 기본 조회 형태
    def _base_query(self):
        return (
            self.db.query(
                Waiting.id,
                Waiting.customer_id,
                Customer.name,
                Customer.phone,
                Waiting.status,
                Waiting.queue_order,
                Waiting.slot_id,
                Waiting.estimated_minutes,
                Waiting.started_at,
            )
            .join(Customer, Customer.id == Waiting.customer_id)
        )
    
    # 대기중인 사람 조회
    def get_waiting_query(self):
        return (
            self._base_query()
            .filter(Waiting.status == WaitingStatus.WAITING)
            .order_by(Waiting.queue_order.asc())
        )

    # 진행중인 사람 조회
    def get_in_progress_query(self):
        return (
            self._base_query()
            .filter(Waiting.status == WaitingStatus.IN_PROGRESS)
        )

    #페이징 처리
    def paginate_waiting(self, page: int, size: int):
        query = self.get_waiting_query()
        result = paginate(query, page, size)

        result["items"] = [self._serialize(row) for row in result["items"]]
        return result
    
    def paginate_in_progress(self, page: int, size: int):
        query = self.get_in_progress_query()
        result = paginate(query, page, size)

        result["items"] = [self._serialize(row) for row in result["items"]]
        return result
    
    # 다음 사람
    def get_next_waiting(self):
        return self.get_waiting_query().first()
    
    def _serialize(self, row):
        return {
            "id": row.id,
            "customer_id": row.customer_id,
            "name": row.name,
            "phone": row.phone,
            "status": row.status,
            "queue_order": row.queue_order,
            "slot_id": row.slot_id,
            "estimated_minutes": row.estimated_minutes,
            "started_at": row.started_at,
        }
        
    # 관리자용 전체 조회
    def get_all(self):
        return [self._serialize(r) for r in self._base_query().all()]
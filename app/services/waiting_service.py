from app.core.pagination import paginate
from app.services.base_service import BaseService
from app.models.waiting_model import Waiting
from app.models.customer_model import Customer
from app.core.enums import WaitingStatus

class WaitingService(BaseService):
    model = Waiting

    # 공통 SELECT
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

    # status 기준 조회 + 페이징
    def paginate_by_status(
        self,
        status: WaitingStatus,
        page: int,
        size: int,
    ):
        query = self._base_query().filter(Waiting.status == status)

        # 대기중일 때만 순서 정렬
        if status == WaitingStatus.WAITING:
            query = query.order_by(Waiting.queue_order.asc())

        result = paginate(query, page, size)
        result["items"] = [self._serialize(row) for row in result["items"]]
        return result

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
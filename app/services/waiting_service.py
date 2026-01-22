from app.services.base_service import BaseService
from app.models.waiting_model import Waiting

class WaitingService(BaseService):
    model = Waiting
    
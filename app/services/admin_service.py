from app.models.admin_model import Admin
from app.services.base_service import BaseService

class AdminService(BaseService[Admin]):
    model = Admin
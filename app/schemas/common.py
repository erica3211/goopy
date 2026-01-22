from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None
    message: str
    

class PageResponse(BaseModel, Generic[T]):
    items: List[T]
    page: int
    size: int
    total: int
    total_pages: int
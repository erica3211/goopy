from typing import Generic, TypeVar, Optional
from app.schemas.common import ApiResponse

T = TypeVar("T")

def success(data: Optional[T] = None, message: str = "success"):
    return ApiResponse(
        success=True,
        data=data,
        message=message
    )

def fail(message: str = "fail"):
    return ApiResponse(
        success=False,
        data=None,
        message=message
    )
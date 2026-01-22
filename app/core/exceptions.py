from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.common import ApiResponse

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(
            success=False,
            data=None,
            message=exc.detail
        ).dict()
    )
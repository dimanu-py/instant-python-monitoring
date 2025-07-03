from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.driving.api_response import Error, ApiError
from src.driving.v1 import routes as v1
from src.monitoring.shared.errors.domain_error import DomainError


app = FastAPI()
app.include_router(v1.router)


@app.exception_handler(Exception)
async def unexpected_exception_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    error = Error(
        type="internal_server_error",
        detail="An unexpected error occurred",
        source=request.url.path,
        base_error=str(exc),
    )
    return ApiError(errors=[error]).to_json(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )


@app.exception_handler(DomainError)
async def domain_error_handler(request: Request, exc: DomainError) -> JSONResponse:
    error = Error(
        type=exc.type,
        detail=exc.message,
        source=request.url.path,
        base_error=str(exc),
    )
    return ApiError(errors=[error]).to_json(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )

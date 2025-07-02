from fastapi import FastAPI, Request

from src.driving.v1 import routes as v1
from src.monitoring.domain_error import DomainError
from src.monitoring.driving.http.responses import (
    InternalServerError,
    HttpResponse,
    UnprocessableEntity,
)

app = FastAPI()
app.include_router(v1.router)


@app.exception_handler(Exception)
async def unexpected_exception_handler(_: Request, exc: Exception) -> HttpResponse:
    return InternalServerError()


@app.exception_handler(DomainError)
async def domain_error_handler(_: Request, exc: DomainError) -> HttpResponse:
    return UnprocessableEntity(message=exc.message)

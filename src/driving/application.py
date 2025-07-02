from fastapi import FastAPI, Request

from src.monitoring.domain_error import DomainError
from src.monitoring.driving.http.responses import (
    InternalServerError,
    HttpResponse,
    UnprocessableEntity,
)

app = FastAPI()


@app.exception_handler(Exception)
async def unexpected_exception_handler(_: Request, exc: Exception) -> HttpResponse:
    return InternalServerError()


@app.exception_handler(DomainError)
async def domain_error_handler(_: Request, exc: DomainError) -> HttpResponse:
    return UnprocessableEntity(message=exc.message)

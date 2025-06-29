from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.monitoring.driving.http.http_response import HttpResponse
from src.monitoring.driving.http.status_code import StatusCode
from src.monitoring.domain_error import DomainError

app = FastAPI()


@app.exception_handler(Exception)
async def unexpected_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    return HttpResponse.internal_error(exc)


@app.exception_handler(DomainError)
async def domain_error_handler(_: Request, exc: DomainError) -> JSONResponse:
    return HttpResponse.domain_error(exc, status_code=StatusCode.BAD_REQUEST)

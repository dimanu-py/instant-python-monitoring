from pydantic import BaseModel, Field
from fastapi import status


class HttpResponse(BaseModel):
    message: str
    status_code: int


class Successful(HttpResponse):
    content: dict
    message: str = Field(init=False, default="Operation successful.")
    status_code: int = Field(init=False, default=status.HTTP_200_OK)


class NotFound(HttpResponse):
    message: str
    status_code: int = Field(init=False, default=status.HTTP_404_NOT_FOUND)


class UnprocessableEntity(HttpResponse):
    message: str
    status_code: int = Field(init=False, default=status.HTTP_422_UNPROCESSABLE_ENTITY)


class TooManyRequests(HttpResponse):
    message: str
    status_code: int = Field(init=False, default=status.HTTP_429_TOO_MANY_REQUESTS)


class InternalServerError(HttpResponse):
    message: str = Field(init=False, default="Internal server error.")
    status_code: int = Field(init=False, default=status.HTTP_500_INTERNAL_SERVER_ERROR)

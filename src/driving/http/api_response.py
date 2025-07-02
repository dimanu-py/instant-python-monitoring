from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi import status


class ApiSuccess(BaseModel):
    data: dict
    success: bool = Field(init=False, default=True)

    def to_json(self, status_code: int = status.HTTP_200_OK) -> JSONResponse:
        return JSONResponse(self.model_dump_json(), status_code=status_code)


class Error(BaseModel):
    type: str
    detail: str
    source: str | None = Field(default=None)
    base_error: str | None = Field(default=None)


class ApiError(BaseModel):
    errors: list[Error]
    success: bool = Field(init=False, default=False)

    def to_json(self, status_code: int) -> JSONResponse:
        return JSONResponse(self.model_dump_json(), status_code=status_code)

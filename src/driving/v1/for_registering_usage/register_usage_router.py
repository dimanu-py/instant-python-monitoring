from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


class RegisterUsageRequest(BaseModel):
    command: str
    version: str
    platform: str
    template_data: dict


@router.post("/usage", status_code=status.HTTP_204_NO_CONTENT)
def register_usage(request: RegisterUsageRequest) -> None:
    raise NotImplementedError


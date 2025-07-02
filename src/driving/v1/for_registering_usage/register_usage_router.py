from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


@router.post("/usage", status_code=status.HTTP_204_NO_CONTENT)
def register_usage(request: RegisterUsageRequest) -> None:
    raise NotImplementedError


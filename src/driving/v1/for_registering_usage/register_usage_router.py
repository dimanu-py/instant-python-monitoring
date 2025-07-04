import os

from fastapi import APIRouter, status
from pydantic import BaseModel

from src.driven.for_sending_usage.loki_client import LokiClient
from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)
from src.monitoring.driving.for_registering_usage.usage_registrar import UsageRegistrar

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


class RegisterUsageRequest(BaseModel):
    command: str
    version: str
    platform: str
    template_data: dict


@router.post("/usage", status_code=status.HTTP_204_NO_CONTENT)
def register_usage(request: RegisterUsageRequest) -> None:
    command = RegisterUsageCommand(**request.model_dump())
    usage_registrar = UsageRegistrar(
        for_sending_usage=LokiClient(
            url=os.environ.get("LOKI_URL"),
            username=os.environ.get("LOKI_USERNAME"),
            password=os.environ.get("LOKI_PASSWORD"),
        ),
    )
    usage_registrar.execute(command)

from dataclasses import dataclass


@dataclass(frozen=True)
class RegisterUsageCommand:
    command: str
    version: str
    platform: str
    template_data: dict

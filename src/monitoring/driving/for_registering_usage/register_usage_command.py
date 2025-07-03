from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class RegisterUsageCommand:
    command: str
    version: str
    platform: str
    template_data: dict

    def to_primitives(self) -> dict:
        return asdict(self)

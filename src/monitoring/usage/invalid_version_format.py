from src.monitoring.shared.errors.domain_error import DomainError


class InvalidVersionFormat(DomainError):
    def __init__(self, value: str) -> None:
        self._message = f"Version '{value}' must be in the format 'major.minor.patch' (e.g., '1.0.0'). "
        self._type = "invalid_version_format"
        super().__init__(self._message, self._type)

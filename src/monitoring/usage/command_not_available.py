from src.monitoring.shared.errors.domain_error import DomainError


class CommandNotAvailable(DomainError):
    def __init__(self, value: str) -> None:
        self._message = f"Command '{value}' is not available to be registered."
        self._type = "command_not_available"
        super().__init__(self._message, self._type)

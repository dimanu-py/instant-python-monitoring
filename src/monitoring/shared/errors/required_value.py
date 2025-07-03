from src.monitoring.shared.errors.domain_error import DomainError


class RequiredValue(DomainError):
    def __init__(self) -> None:
        self._message = "Value is required, can't be None"
        self._type = "validation_error.required_value"
        super().__init__(message=self._message, error_type=self._type)

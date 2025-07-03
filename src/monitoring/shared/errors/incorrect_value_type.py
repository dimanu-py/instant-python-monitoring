from typing import TypeVar

from src.monitoring.shared.errors.domain_error import DomainError

T = TypeVar("T")


class IncorrectValueType(DomainError):
    def __init__(self, value: T) -> None:
        self._message = f"Value '{value}' is not of type {type(value).__name__}"
        self._type = "validation_error.incorrect_value_type"
        super().__init__(message=self._message, error_type=self._type)

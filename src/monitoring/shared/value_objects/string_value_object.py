from typing import override

from src.monitoring.shared.errors.incorrect_value_type import IncorrectValueType
from src.monitoring.shared.errors.required_value import RequiredValue
from src.monitoring.shared.value_objects.value_object import ValueObject


class StringValueObject(ValueObject[str]):
    def __init__(self, value: str) -> None:
        super().__init__(value)

    @override
    def _validate(self) -> None:
        self._ensure_has_value()
        self._ensure_is_string()

    def _ensure_is_string(self) -> None:
        if not isinstance(self._value, str):
            raise IncorrectValueType(value=self._value)

    def _ensure_has_value(self) -> None:
        if self._value is None:
            raise RequiredValue()

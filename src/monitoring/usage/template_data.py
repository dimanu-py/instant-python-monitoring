from typing import override

from src.monitoring.shared.errors.incorrect_value_type import IncorrectValueType
from src.monitoring.shared.errors.required_value import RequiredValue
from src.monitoring.shared.value_objects.value_object import ValueObject
from src.monitoring.usage.missing_template_keys import MissingTemplateKeys


class TemplateData(ValueObject[dict]):
    _REQUIRED_KEYS = ["name", "built_in_features"]

    def __init__(self, value: dict) -> None:
        super().__init__(value)

    @override
    def _validate(self) -> None:
        self._ensure_has_value()
        self._ensure_is_dict()
        self._ensure_has_required_keys()

    def _ensure_has_value(self) -> None:
        if self._value is None:
            raise RequiredValue()

    def _ensure_is_dict(self) -> None:
        if not isinstance(self._value, dict):
            raise IncorrectValueType(value=self._value)

    def _ensure_has_required_keys(self) -> None:
        missing_keys = set(self._REQUIRED_KEYS) - set(self._value.keys())
        if missing_keys:
            raise MissingTemplateKeys(missing_keys=missing_keys)

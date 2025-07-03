import re
from typing import override

from src.monitoring.shared.value_objects.string_value_object import StringValueObject
from src.monitoring.usage.invalid_version_format import InvalidVersionFormat


class Version(StringValueObject):
    def __init__(self, value: str) -> None:
        super().__init__(value)

    @override
    def _validate(self) -> None:
        super()._validate()
        self._ensure_version_format()

    def _ensure_version_format(self) -> None:
        if not re.match(r'^\d+\.\d+\.\d+$', self.value):
            raise InvalidVersionFormat(self._value)

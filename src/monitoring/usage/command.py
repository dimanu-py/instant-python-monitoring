from typing import override

from src.monitoring.shared.value_objects.string_value_object import StringValueObject
from src.monitoring.usage.command_not_available import CommandNotAvailable


class Command(StringValueObject):
    _AVAILABLE_COMMANDS = ["init", "config"]

    def __init__(self, value: str) -> None:
        super().__init__(value)

    @override
    def _validate(self) -> None:
        super()._validate()
        self._ensure_command_is_supported()

    def _ensure_command_is_supported(self) -> None:
        if self._value not in self._AVAILABLE_COMMANDS:
            raise CommandNotAvailable(self._value)

import pytest
from expects import expect, raise_error

from src.monitoring.usage.command import Command
from src.monitoring.usage.command_not_available import CommandNotAvailable


@pytest.mark.unit
class TestCommand:
    def test_should_raise_error_when_creating_not_available_command(self) -> None:
        expect(lambda: Command("not_available_command")).to(
            raise_error(CommandNotAvailable)
        )

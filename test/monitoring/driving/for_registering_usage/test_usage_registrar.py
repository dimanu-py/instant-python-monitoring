import pytest
from doublex import Spy, assert_that, called

from src.monitoring.driven.for_sending_usage.for_sending_usage import ForSendingUsage
from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)
from src.monitoring.driving.for_registering_usage.usage_registrar import UsageRegistrar


@pytest.mark.unit
class TestUsageRegistrar:
    def test_should_register_command_usage(self) -> None:
        command = RegisterUsageCommand(
            command="init",
            version="0.8.0",
            platform="linux",
            template_data={
                "name": "standard_project",
                "built_in_features": ["logger", "makefile"],
            },
        )
        sender = Spy(ForSendingUsage)
        usage_registrar = UsageRegistrar(for_sending_usage=sender)  # type: ignore

        usage_registrar.execute(command)

        self._should_have_send_usage_information(command.to_primitives(), sender)

    def _should_have_send_usage_information(self, expected_information: dict, sender) -> None:
        assert_that(
            sender.send_information,
            called().with_args(info=expected_information),
        )

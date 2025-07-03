import pytest
from doublex import Spy, assert_that, called

from src.monitoring.driven.for_sending_usage.for_sending_usage import ForSendingUsage
from src.monitoring.driving.for_registering_usage.usage_registrar import UsageRegistrar
from src.monitoring.usage.usage_information import UsageInformationPrimitives, UsageInformation
from test.monitoring.driving.for_registering_usage.register_usage_command_mother import RegisterUsageCommandMother
from test.monitoring.usage.usage_information_primitives_mother import UsageInformationPrimitivesMother


@pytest.mark.unit
class TestUsageRegistrar:
    def setup_method(self) -> None:
        self._sender = Spy(ForSendingUsage)
        self._usage_registrar = UsageRegistrar(for_sending_usage=self._sender)  # type: ignore

    def test_should_register_command_usage(self) -> None:
        command = RegisterUsageCommandMother.any()
        usage_information_primitives = UsageInformationPrimitivesMother.from_command(command)

        self._usage_registrar.execute(command)

        self._should_have_send_usage_information(usage_information_primitives)

    def _should_have_send_usage_information(self, expected_information: UsageInformationPrimitives) -> None:
        assert_that(
            self._sender.send_information,
            called().with_args(info=UsageInformation(**expected_information)),
        )

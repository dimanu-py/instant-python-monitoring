from src.monitoring.driven.for_sending_usage.for_sending_usage import ForSendingUsage
from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)


class UsageRegistrar:
    def __init__(self, for_sending_usage: ForSendingUsage) -> None:
        self._sender = for_sending_usage

    def execute(self, command: RegisterUsageCommand) -> None:
        self._sender.send_information(info=command.to_primitives())

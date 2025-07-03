from src.monitoring.driven.for_sending_usage.for_sending_usage import ForSendingUsage
from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)
from src.monitoring.usage.usage_information import UsageInformation


class UsageRegistrar:
    def __init__(self, for_sending_usage: ForSendingUsage) -> None:
        self._sender = for_sending_usage

    def execute(self, command: RegisterUsageCommand) -> None:
        usage_information = UsageInformation(
            command=command.command,
            version=command.version,
            platform=command.platform,
            template_data=command.template_data,
        )
        self._sender.send_information(info=usage_information)

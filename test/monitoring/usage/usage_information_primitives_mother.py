from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)
from src.monitoring.usage.usage_information import UsageInformationPrimitives


class UsageInformationPrimitivesMother:
    @staticmethod
    def from_command(command: RegisterUsageCommand) -> UsageInformationPrimitives:
        return UsageInformationPrimitives(
            command=command.command,
            version=command.version,
            platform=command.platform,
            template_data=command.template_data,
        )

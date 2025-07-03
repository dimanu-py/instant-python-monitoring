from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)
from src.monitoring.usage.usage_information import UsageInformationPrimitives
from test.monitoring.usage.command_primitives_mother import CommandPrimitivesMother
from test.random_generator import RandomGenerator


class UsageInformationPrimitivesMother:
    @staticmethod
    def any() -> UsageInformationPrimitives:
        return UsageInformationPrimitives(
            command=CommandPrimitivesMother.any(),
            version=RandomGenerator.version(),
            platform=RandomGenerator.operating_system(),
            template_data={
                "name": "standard_project",
                "built_in_features": ["logger", "makefile"],
            },
        )

    @staticmethod
    def from_command(command: RegisterUsageCommand) -> UsageInformationPrimitives:
        return UsageInformationPrimitives(
            command=command.command,
            version=command.version,
            platform=command.platform,
            template_data=command.template_data,
        )

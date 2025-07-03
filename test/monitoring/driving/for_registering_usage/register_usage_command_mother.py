from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)
from test.random_generator import RandomGenerator


class RegisterUsageCommandMother:
    @staticmethod
    def any() -> RegisterUsageCommand:
        return RegisterUsageCommand(
            command=RandomGenerator.command_name(),
            version=RandomGenerator.version(),
            platform=RandomGenerator.operating_system(),
            template_data={
                "name": "standard_project",
                "built_in_features": ["logger", "makefile"],
            },
        )

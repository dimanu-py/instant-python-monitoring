from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)
from test.monitoring.usage.command_primitives_mother import CommandPrimitivesMother
from test.random_generator import RandomGenerator


class RegisterUsageCommandMother:
    @staticmethod
    def any() -> RegisterUsageCommand:
        return RegisterUsageCommand(
            command=CommandPrimitivesMother.any(),
            version=RandomGenerator.version(),
            platform=RandomGenerator.operating_system(),
            template_data={
                "name": "standard_project",
                "built_in_features": ["logger", "makefile"],
            },
        )

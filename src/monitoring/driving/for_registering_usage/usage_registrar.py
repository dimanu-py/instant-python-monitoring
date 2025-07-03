from src.monitoring.driving.for_registering_usage.register_usage_command import (
    RegisterUsageCommand,
)


class UsageRegistrar:
    def execute(self, command: RegisterUsageCommand) -> None:
        raise NotImplementedError

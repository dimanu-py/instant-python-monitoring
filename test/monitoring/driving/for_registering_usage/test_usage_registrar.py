import pytest


@pytest.mark.unit
class TestUsageRegistrar:
    @pytest.mark.xfail
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
        usage_registrar = UsageRegistrar()

        usage_registrar.execute(command)

        self._should_have_send_usage_information()

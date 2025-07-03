from src.monitoring.usage.command import Command
from src.monitoring.usage.platform import Platform
from src.monitoring.usage.template_data import TemplateData
from src.monitoring.usage.version import Version


class UsageInformation:
    def __init__(
        self, command: str, version: str, platform: str, template_data: dict
    ) -> None:
        self._command = Command(command)
        self._version = Version(version)
        self._platform = Platform(platform)
        self._template_data = TemplateData(template_data)

from typing import TypedDict, Self

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

    @property
    def value(self) -> "UsageInformationPrimitives":
        return UsageInformationPrimitives(
            command=self._command.value,
            version=self._version.value,
            platform=self._platform.value,
            template_data=self._template_data.value,
        )

    @property
    def command(self) -> Command:
        return self._command

    @property
    def version(self) -> Version:
        return self._version

    def __eq__(self, other: Self) -> bool:
        return self.value == other.value


class UsageInformationPrimitives(TypedDict):
    command: str
    version: str
    platform: str
    template_data: dict

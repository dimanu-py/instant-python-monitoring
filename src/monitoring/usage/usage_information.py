class UsageInformation:
    def __init__(self, command: str, version: str, platform: str, template_data: dict) -> None:
        self._command = command
        self._version = version
        self._platform = platform
        self._template_data = template_data

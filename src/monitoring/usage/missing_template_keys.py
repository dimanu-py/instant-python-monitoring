from src.monitoring.shared.errors.domain_error import DomainError


class MissingTemplateKeys(DomainError):
    def __init__(self, missing_keys: set) -> None:
        self._message = f"Missing required template keys: {', '.join(missing_keys)}"
        self._type = "missing_template_keys"
        super().__init__(self._message, self._type)

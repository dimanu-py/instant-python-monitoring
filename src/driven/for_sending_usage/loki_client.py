from src.monitoring.driven.for_sending_usage.for_sending_usage import ForSendingUsage


class LokiClient(ForSendingUsage):
    def __init__(self, url: str) -> None:
        self._url = url

    def send_information(self, info: dict) -> None:
        raise NotImplementedError()

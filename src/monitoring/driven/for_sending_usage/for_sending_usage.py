from abc import ABC, abstractmethod

from src.monitoring.usage.usage_information import UsageInformation


class ForSendingUsage(ABC):
    @abstractmethod
    def send_information(self, info: UsageInformation) -> None:
        raise NotImplementedError

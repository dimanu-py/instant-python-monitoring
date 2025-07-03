from abc import ABC, abstractmethod


class ForSendingUsage(ABC):
    @abstractmethod
    def send_information(self, info: dict) -> None:
        raise NotImplementedError

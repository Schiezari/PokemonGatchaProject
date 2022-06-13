from abc import ABC, abstractmethod


class IEventProvider(ABC):
    @abstractmethod
    def call_back(self, err, msg):
        pass

    @abstractmethod
    def send(self, message: str):
        pass

from abc import ABC, abstractmethod
from xmlrpc.client import Boolean

class Engine(ABC):
        
    @abstractmethod
    def engine_should_be_serviced(self) -> Boolean:
        pass
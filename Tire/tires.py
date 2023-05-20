

from abc import ABC, abstractmethod


class Tires(ABC):
    def __init__(self,tirearr):
        self.arr=tirearr
    @abstractmethod
    def service_needed(self):
        pass

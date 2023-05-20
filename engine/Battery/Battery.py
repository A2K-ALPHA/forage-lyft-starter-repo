from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self,Last_service_date,current_date):
        self.Last_service_date=Last_service_date
        self.current_date=current_date
    @abstractmethod
    def Needs_service(self):
        pass
class SplinderBattery(Battery):
    def __init__(self, Last_service_date, current_date):
        super().__init__(Last_service_date, current_date)
    def Needs_service(self):
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if self.service_threshold_date<self.current_date:
            return True
        else:
            return False
class NubbinBattery(Battery):
    def __init__(self, Last_service_date, current_date):
        super().__init__(Last_service_date, current_date)
    def Needs_service(self):
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if self.service_threshold_date<self.current_date:
            return True
        else:
            return False

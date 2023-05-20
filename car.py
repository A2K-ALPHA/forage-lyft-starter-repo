from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, Engine_used,Battery_used,Tire_used):
        self.Engine_used=Engine_used
        self.Battery_used=Battery_used
        self.Tire_used=Tire_used

    
    def needs_service(self):
        
        if self.Engine_used.engine_should_be_serviced() or self.Battery_used.Needs_service() or self.Tire_used.service_needed():
            return True
        else:
            return False

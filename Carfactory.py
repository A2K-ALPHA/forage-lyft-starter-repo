
from Tire.carrigan import carrigan_tires
from Tire.Octotire import Octo_tires 
from car import Car as car
from engine.capulet_engine import CapuletEngine

from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from Battery.Battery import SplinderBattery
from Battery.Battery import NubbinBattery
class CarFactory:
    def __init__(self):
        pass
    
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage,Tirearr):
        self.cal=car(CapuletEngine(current_mileage,last_service_mileage), SplinderBattery(last_service_date,current_date),carrigan_tires(Tirearr))
        return self.cal
    
    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage,Tirearr):
        self.glis=car(WilloughbyEngine(current_mileage,last_service_mileage), SplinderBattery(last_service_date,current_date),Octo_tires(Tirearr))
        return self.glis
    def create_Pallindrome(self,current_date, last_service_date, warning_light_is_on,Tirearr):
        self.pal=car(SternmanEngine(warning_light_is_on),NubbinBattery(last_service_date,current_date),carrigan_tires(Tirearr))
        return self.pal
    
    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage,Tirearr):
        self.ror=car(WilloughbyEngine(current_mileage,last_service_mileage),NubbinBattery(last_service_date,current_date),Octo_tires(Tirearr))
        return self.ror
    def create_Thovex(self,current_date, last_service_date, current_mileage, last_service_mileage,Tirearr):
        self.thov=car(CapuletEngine(current_mileage,last_service_mileage),NubbinBattery(last_service_date,current_date),carrigan_tires(Tirearr))
        
        return self.thov
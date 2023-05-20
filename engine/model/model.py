
import imp
from car import car
from capulet_engine import CapuletEngine
from engine import willoughby_engine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from Battery import Battery
class CarFactory:
    def __init__(self):
        pass
    
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.cal=car(CapuletEngine(current_mileage,last_service_mileage), Battery.SplinderBattery(last_service_date,current_date))
        return self.cal
    
    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.glis=car(WilloughbyEngine(current_mileage,last_service_mileage), Battery.SplinderBattery(last_service_date,current_date))
        return self.glis
    def create_Pallindrome(self,current_date, last_service_date, warning_light_is_on):
        self.pal=car(SternmanEngine(self,warning_light_is_on), Battery.NubbinBattery(last_service_date,current_date))
        return self.pal
    
    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.ror=car(WilloughbyEngine(current_mileage,last_service_mileage), Battery.NubbinBattery(last_service_date,current_date))
        return self.ror
    def create_Thovex(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.thov=car(CapuletEngine(current_mileage,last_service_mileage), Battery.SplinderBattery(last_service_date,current_date))
        
        return self.thov
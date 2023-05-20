from Tire.tires import Tires

class Octo_tires(Tires):
    def __init__(self, tirearr):
        super().__init__(tirearr)
    def service_needed(self):
        return sum(self.arr)>=3
from Tire.tires import Tires

class carrigan_tires(Tires):
    def __init__(self, tirearr):
        super().__init__(tirearr)
    def service_needed(self):
        return max(self.arr)>=0.9
from car_park import CarPark
from random import randint
class Sensor:
    def __init__(self, id = None, is_active = False, car_park = CarPark()):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park



class EntrySensor(Sensor):
    ...
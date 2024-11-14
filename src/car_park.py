from sensor import Sensor
from display import Display
from random import randint

class CarPark:
    def __init__(self, location = "undefined",
                 capacity = 100,
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        """
        Return CarPark object formatted as string.
        :return: string
        """
        # e.g. "Car park at 123 Example Street, with 100 bays.".
        return f"Car park at {self.location}, with {self.capacity} total bays"

    def register(self, component):
        if type(component) is Sensor:
            self.sensors.append(component)
        elif type(component) is Display:
            self.displays.append(component)
        else:
            raise TypeError("Component must be either a Sensor or Display")

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        data = {available_bays: self.available_bays}


    def check_plate_in_car_park(self):
        pass

    @property
    def available_bays(self):
        bays = self.capacity - len(self.plates)
        return bays if bays > 0 else 0

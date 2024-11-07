from sensor import Sensor
from display import Display

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

    def add_car(self):
        pass

    def remove_car(self):
        pass

    def update_displays(self):
        pass

    def check_plate_in_car_park(self):
        pass
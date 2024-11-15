from display import Display
from random import randint, choice
from sensor import ExitSensor, EntrySensor

class CarPark:
    def __init__(self, location="undefined",
                 capacity=100,
                 plates=None,
                 entry_sensors=None,
                 exit_sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.entry_sensors = entry_sensors or []
        self.exit_sensors = exit_sensors or []
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        """
        Return CarPark object formatted as string.
        :return: string
        """
        # e.g. "Car park at 123 Example Street, with 100 bays.".
        return f"Car park at {self.location}, with {self.capacity} total bays"


    # def update_car_park(self, plate):
    #     plate = self._scan_plate()
    #     self.car_park.add_car(plate)
    #     print(f"Incoming 🚘 vehicle detected. Plate: {plate}")
    #     self.car_park.update_displays()
    #
    # def update_car_park(self, plate):
    #     for sensor in self.car_park.sensors:
    #         sensor.car_park = self.car_park

    def register(self, component):
        if type(component) is EntrySensor:
            self.entry_sensors.append(component)
        elif type(component) is ExitSensor:
            self.exit_sensors.append(component)
        elif type(component) is Display:
            self.displays.append(component)
        else:
            raise TypeError("Component must be either a Sensor or Display")

    def add_car(self, plate):
        self.plates.append(plate)

    def remove_car(self, plate):
        if self.check_plate_in_car_park(plate):
            self.plates.remove(plate)
        else:
            raise ValueError("Cannot remove car not in car park.")

    def update_displays(self):
        data = {}
        sensors = self.entry_sensors + self.exit_sensors
        for i, sensor in enumerate(sensors):
            data[f'sensor#{i}'] = sensor.id
        for i, display in enumerate(self.displays):
            data[f'display#{i}'] = display.id
        for i, plate in enumerate(self.plates):
            data[f'plate#{i}'] = plate
        for display in self.displays:
            display.update(data)

    def check_plate_in_car_park(self, plate):
        return plate in self.plates

    @property
    def available_bays(self):
        bays = self.capacity - len(self.plates)
        return bays if bays > 0 else 0

    def detect_vehicle_entry(self):
        if len(self.entry_sensors) > 0:
            plate = choice(self.entry_sensors).scan_plate()
            self.plates.append(plate)

    def detect_vehicle_exit(self):
        if len(self.entry_sensors) > 0:
            plate = choice(self.exit_sensors).scan_plate(self.plates)
            self.plates.remove(plate)
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
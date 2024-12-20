import time
class Display:
    def __init__(self, id = None, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: Welcome to the car park."

    def get_current_time(self):
        return time.localtime()

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")

    @property
    def temperature(self):
        # randomly generate a reasonable temperature in degrees celsius
        return 23
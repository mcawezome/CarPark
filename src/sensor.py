from car_park import CarPark
from random import randint
class Sensor:
    def __init__(self, id = None, is_active = False, car_park = CarPark()):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def scan_plate(self):
        number_plate = ""
        first_digit = randint(0,9)
        number_plate += str(first_digit)

        # A-Z in ASCII is between 65-90
        letters = [ord(randint(65,90)) for _ in range(0,2)]
        for letter in letters:
            number_plate += letter
        # add 3 digits to the end of number plate
        last_digits = randint(0,999)
        add_string = ""

        if last_digits < 100:
            # if number 001 - 009
            if last_digits < 10:
                add_string = "00"
            # if number 010 - 099
            else:
                add_string = "0"

        number_plate += add_string + str(last_digits)

        return number_plate


class EntrySensor(Sensor):
    ...

class ExitSensor(Sensor):
    ...
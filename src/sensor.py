from random import randint, choice
from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, id = None, is_active = False):
        self.id = id
        self.is_active = is_active


    @abstractmethod
    def scan_plate(self):
        pass



class EntrySensor(Sensor):
    def __init__(self, id = None, is_active = False):
        super().__init__(id, is_active)
    def scan_plate(self):
        """
        Returns a random number plate in form "1ABC123"

        :return: number_plate (string)
        """
        number_plate = ""
        first_digit = randint(0,9)
        number_plate += str(first_digit)

        # A-Z in ASCII is between 65-90
        letters = [chr(randint(65,90)) for _ in range(0,3)]
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




class ExitSensor(Sensor):
    def __init__(self, id = None, is_active = False):
        super().__init__(id, is_active)

    def scan_plate(self, plates):
        if len(plates) > 0:
            return choice(plates)
        else:
            raise ValueError("Cannot remove car from empty car park.")
import unittest
from display import Display
from car_park import CarPark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark()
        self.display = Display(1, "Welcome to the car park", True)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)

    def test_temperature(self):
        temp = self.display.temperature
        self.assertEqual(temp, 23)
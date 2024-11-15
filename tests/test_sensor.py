import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark()
        self.sensor1 = EntrySensor(1, True)
        self.sensor2 = EntrySensor(1, True)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor1, Sensor)
        self.assertIsInstance(self.sensor1, EntrySensor)
        self.assertEqual(self.sensor1.id, 1)
        self.assertEqual(self.sensor1.is_active, True)


    def test_sensor_scan_plate(self):
        plate1 = self.sensor1.scan_plate()
        self.assertEqual(len(plate1), 7)
        self.assertIsInstance(plate1, str)
        plate2 = self.sensor2.scan_plate()
        # assert exit sensor removed plate1
        self.assertEqual(plate1, plate2)
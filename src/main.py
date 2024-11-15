from car_park import EntrySensor, ExitSensor
from display import Display
from car_park import CarPark

if __name__ == "__main__":
    sensor1 = EntrySensor()
    sensor2 = ExitSensor()
    display1 = Display()
    car_park = CarPark()

    car_park.register(sensor1)
    car_park.register(sensor2)
    car_park.register(display1)
    car_park.detect_vehicle_entry()
    car_park.detect_vehicle_entry()
    car_park.detect_vehicle_entry()
    car_park.detect_vehicle_entry()
    car_park.detect_vehicle_exit()
    car_park.update_displays()

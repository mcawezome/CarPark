from car_park import EntrySensor, ExitSensor
from display import Display
from car_park import CarPark

if __name__ == "__main__":
    sensor1 = EntrySensor(1, True)
    sensor2 = ExitSensor(2, True)
    display1 = Display(1, "Welcome to Moondalup", True)
    car_park = CarPark("moondalup", 100, log_file="moondalup.txt")


    car_park.register(sensor1)
    car_park.register(sensor2)
    car_park.register(display1)
    for _ in range(10):
        car_park.detect_vehicle_entry()

    car_park.detect_vehicle_exit()
    car_park.detect_vehicle_exit()

    car_park.update_displays()

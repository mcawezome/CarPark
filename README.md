Task 3: Update the README.md file with a brief project description.

**Car Park Application**

This python application is a demonstration of object-oriented principles.
The program aims to implement an automated carp park
which tracks number of cars, check sensors and updates displays.

The code base is divided into src and tests, in order to unit test the code.
Any and all evidence of work is put into the evidence folder.


| Class Name | Attributes                                                 | Methods                                                                                                                          |
| ---------- |------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `CarPark`    | location<br/>capacity<br/>platess<br/>sensors<br/>displays | __str__()<br/>register()<br/>add_car()<br/>remove_car()<br/>update_displays()<br/>check_plate_in_car_park()<br/>available_bays() |
| `Sensor`     | id<br/>is_active<br/>car_park                              |                                                                                                                                  |
| `Display`    | id<br/>message<br/>is_on<br/>car_park                      | __str__()<br/>get_current_time()<br/>update()<br/>temperature()                                                                  |
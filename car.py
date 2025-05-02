import re
from datetime import *

class Car:
    def __init__(self, car_number, time):
        self.car_type = None
        self.license_plate = self.validate(car_number)
        self.timestamp = time

    @staticmethod
    def validate(plate):
        pattern = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'
        if not re.fullmatch(pattern, plate.upper()):
            raise ValueError(f'Некорректный знак: {plate}')
        return plate.upper()

    def to_array(self):
        return (self.car_type, self.timestamp.strftime('%d.%m.%Y'), self.timestamp.strftime('%H:%M'), self.license_plate)

    def print(self):
        return f'{self.car_type} - {self.timestamp.strftime("%d.%m.%Y %H:%M")} - {self.license_plate}'

class PassengerCar(Car):
    def __init__(self, car_number, time):
        super().__init__(car_number, time)
        self.car_type = 'passenger'


class TruckCar(Car):
    def __init__(self, car_number, time):
        super().__init__(car_number, time)
        self.car_type = 'truck'


if __name__ == "__main__":
    cars = []

    cars.append(PassengerCar("А123ОВ777", datetime(2023, 5, 10, 8, 15)))
    cars.append(TruckCar("У456ХХ78", datetime(2023, 5, 10, 9, 30)))
    cars.append(TruckCar("Е789МН123", datetime(2023, 5, 11, 12, 45)))

    print("Все записи в реестре:")
    for car in cars:
        print(car.print())
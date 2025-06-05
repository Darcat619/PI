from datetime import datetime
import utils

class Car:
    def __init__(self, car_number, time, color):
        self.car_type = None
        self.car_number = self.validate(car_number)
        self.timestamp = time
        self.color = color

    @staticmethod
    def validate(plate):
        return utils.validate_plate(plate)

    def to_tuple(self):
        return (self.car_type, self.timestamp.strftime('%d.%m.%Y'), self.timestamp.strftime('%H:%M'), self.car_number, self.color)

    def print(self):
        return f'{self.car_type} - {self.timestamp.strftime("%d.%m.%Y %H:%M")} - {self.car_number} - {self.color}'

class PassengerCar(Car):
    def __init__(self, car_number, time, color):
        super().__init__(car_number, time, color)
        self.car_type = 'passenger'

class TruckCar(Car):
    def __init__(self, car_number, time, color):
        super().__init__(car_number, time, color)
        self.car_type = 'truck'
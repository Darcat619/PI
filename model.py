from datetime import datetime
from car import Car, PassengerCar, TruckCar

class Model:
    def __init__(self):
        self.cars = []

    def add_car(self, type, car_number, time):
        if time is None:
            time = datetime.now()

        if type == 'passenger':
            car = PassengerCar(car_number, time)
        elif type == 'truck':
            car = TruckCar(car_number, time)
        
        self.cars.append(car)
        return car

    def remove_car(self, index):
        del self.cars[index]

    def get_all_cars(self):
        return self.cars

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split()
                    type = parts[0]
                    date = parts[1]
                    time = parts[2]
                    car_number = parts[3]
                    dt = datetime.strptime(f'{date} {time}', '%d.%m.%Y %H:%M')
                    self.add_car(type, car_number, dt)

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for record in self.cars:
                file.write(f'{" ".join(record.to_array())}\n')
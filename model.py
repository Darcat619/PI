import logging
from datetime import datetime
from car import Car, PassengerCar, TruckCar

# Настройка логирования
logging.basicConfig(filename='car_log.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Model:
    def __init__(self):
        self.cars = []

    def add_car(self, type, car_number, time, color):
        if time is None:
            time = datetime.now()

        try:
            if type == 'passenger':
                car = PassengerCar(car_number, time, color)
            elif type == 'truck':
                car = TruckCar(car_number, time, color)
            else:
                raise ValueError(f'Некорректный тип автомобиля: {type}')
            self.cars.append(car)
            return car
        except ValueError as e:
            logging.error(f"Ошибка при добавлении автомобиля: {str(e)}")
            return None

    def remove_car(self, index):
        try:
            del self.cars[index]
        except IndexError:
            logging.error(f"Ошибка удаления: индекс {index} вне диапазона")
            raise

    def get_all_cars(self):
        return self.cars

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:
                    try:
                        parts = line.split()
                        if len(parts) < 4:
                            raise ValueError(f"Недостаточно данных в строке {line_num}: {line}")
                        type = parts[0]
                        date = parts[1]
                        time = parts[2]
                        car_number = parts[3]
                        color = parts[4] if len(parts) > 4 else "Не указан"
                        dt = datetime.strptime(f'{date} {time}', '%d.%m.%Y %H:%M')
                        car = self.add_car(type, car_number, dt, color)
                        if car is None:
                            raise ValueError(f"Не удалось добавить автомобиль из строки {line_num}: {line}")
                    except ValueError as e:
                        logging.error(f"Ошибка обработки строки {line_num}: {str(e)}")
                    except Exception as e:
                        logging.error(f"Неожиданная ошибка в строке {line_num}: {str(e)}")

    def save_to_file(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for car in self.cars:
                    file.write(f'{" ".join(car.to_tuple())}\n')
        except Exception as e:
            logging.error(f"Ошибка сохранения в файл: {str(e)}")
            raise
import unittest
from datetime import datetime
from model import Model
from car import Car, PassengerCar, TruckCar

class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.valid_time = datetime(2025, 6, 5, 18, 2)  # 06:02 PM CEST, 05.06.2025

    def test_add_car(self):
        car = self.model.add_car('passenger', 'А123АА123', self.valid_time, 'Красный')
        self.assertIsInstance(car, PassengerCar)
        self.assertEqual(len(self.model.get_all_cars()), 1)
        self.assertEqual(car.car_number, 'А123АА123')
        self.assertEqual(car.color, 'Красный')

    def test_add_invalid_car_type(self):
        car = self.model.add_car('bus', 'А123АА123', self.valid_time, 'Красный')
        self.assertIsNone(car)
        self.assertEqual(len(self.model.get_all_cars()), 0)

    def test_remove_car(self):
        car = self.model.add_car('truck', 'Е789ММ123', self.valid_time, 'Синий')
        self.assertEqual(len(self.model.get_all_cars()), 1)
        self.model.remove_car(0)
        self.assertEqual(len(self.model.get_all_cars()), 0)

    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError):
            self.model.remove_car(0)

    def test_load_from_file(self):
        with open('test_data.txt', 'w', encoding='utf-8') as f:
            f.write('passenger 05.06.2025 18:02 А123АА123 Красный\n')
            f.write('truck 05.06.2025 18:03 Е789ММ123 Синий\n')
            f.write('invalid 05.06.2025 18:04 X123XX123 Green\n')
        self.model.load_from_file('test_data.txt')
        cars = self.model.get_all_cars()
        self.assertEqual(len(cars), 2)
        self.assertEqual(cars[0].car_type, 'passenger')
        self.assertEqual(cars[1].car_type, 'truck')

if __name__ == '__main__':
    unittest.main()
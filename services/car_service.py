from exceptions import ExposeException
import json
from models.car import Car

class CarService:
    def __init__(self):
        self.cars = []
        self.load_cars()

    def add_car(self, make, model, year, price):
        id = len(self.cars) + 1
        car = Car(make, model, int(year), int(price), id)

        self.cars.append(car)
        self.save_cars()

    def remove_car(self, id):
        try:
            car_to_remove = next((car for car in self.cars if car._id == id), None)
            if not car_to_remove:
                raise ExposeException("Car not found. Please provide a valid id.")

            self.cars.remove(car_to_remove)

            self.save_cars()
        except ValueError:
            raise ExposeException("Car not found. Please provide a valid id.")

    def update_car(self, id, make, model, year, price):
        car_to_update = next((car for car in self.cars if car._id == id), None)
        if not car_to_update:
            raise ExposeException("Car not found. Please provide a valid id.")

        car_to_update.make = make
        car_to_update.model = model
        car_to_update.year = int(year)
        car_to_update._price = float(price)

        self.save_cars()

    def get_cars(self):
        if self.cars:
            return self.cars
        else:
            return []

    def save_cars(self):
        cars_data = [car.__dict__ for car in self.cars]
        with open('data/cars.json', 'w') as f:
            json.dump(cars_data, f)


    def load_cars(self):
        try:
            with open('data/cars.json', 'r') as f:
                cars_data = json.load(f)
            for car in cars_data:
                self.cars.append(Car(**car))
        except FileNotFoundError:
            raise FileNotFoundError("The cars.json file was not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("The cars.json file contains invalid JSON.")


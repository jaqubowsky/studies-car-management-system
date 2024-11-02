import json
from models.car import Car

class CarService:
    def __init__(self):
        self.cars = []
        self.load_cars()

    def add_car(self, make, model, year, price):
        if not all([make, model, year.isdigit(), price.isdigit()]):
            print("Invalid data. Make, model, and a numeric year are required.")
            return False

        id = len(self.cars) + 1
        car = Car(make, model, int(year), int(price), id)
        self.cars.append(car)
        self.save_cars()
        print(f"{car} added successfully.")

    def remove_car(self, id):
        try:
            id = int(id)
        except ValueError:
            print(f"Invalid id '{id}'. Please provide a numeric value.")
            return None

        if id < 1 or id > len(self.cars):
            print(f"Invalid index {id}. No car removed.")
            return None

        car = self.cars.pop(id - 1)
        self.save_cars()
        print(f"{car} removed successfully.")

    def list_cars(self):
        if self.cars:
            print("Current cars in the system:")
            for _, car in enumerate(self.cars):
                print(f"{car._id}: {car}")
        else:
            print("No cars in the system.")

    def save_cars(self):
        cars_data = [car.__dict__ for car in self.cars]
        with open('cars.json', 'w') as f:
            json.dump(cars_data, f)

    def load_cars(self):
        try:
            with open('cars.json', 'r') as f:
                cars_data = json.load(f)
            for car in cars_data:
                self.cars.append(Car(**car))
        except FileNotFoundError:
            self.cars = []
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty list.")
            self.cars = []


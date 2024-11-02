from models.car import Car

class CarService:
    def __init__(self):
        self.cars = []

    def add_car(self, make, model, year, price):
        if not all([make, model, year.isdigit(), price.isdigit()]):
            print("Invalid data. Make, model, and a numeric year are required.")
            return False

        car = Car(make, model, int(year), int(price))
        self.cars.append(car)
        print(f"{car} added successfully.")

    def remove_car(self, index):
        try:
            index = int(index)
        except ValueError:
            print(f"Invalid index '{index}'. Please provide a numeric value.")
            return None

        if index < 1 or index > len(self.cars):
            print(f"Invalid index {index}. No car removed.")
            return None

        car = self.cars.pop(index - 1)
        print(f"{car} removed successfully.")

    def list_cars(self):
        if self.cars:
            print("Current cars in the system:")
            for index, car in enumerate(self.cars):
                print(f"{index + 1}: {car}")
        else:
            print("No cars in the system.")

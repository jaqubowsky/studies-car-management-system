class Car:
    def __init__(self, make, model, year, price=0):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price:,.2f}"

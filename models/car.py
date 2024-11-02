
class Car:
    def __init__(self, make: str, model: str, year: int, _price: float = 0, _id: int = 0):
        self._id = _id
        self.make = make
        self.model = model
        self.year = year
        self._price = _price

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} - ${self._price:,.2f}"

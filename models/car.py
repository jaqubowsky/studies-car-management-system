
class Car:
    def __init__(self, make: str, model: str, year: int, _price: float = 0, _id: int = 0):
        self._id = _id
        self.make = make
        self.model = model
        self.year = year
        self._price = _price

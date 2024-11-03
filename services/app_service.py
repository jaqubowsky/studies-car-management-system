from exceptions import ExposeException

class AppService:
    def __init__(self, car_service):
        self.car_service = car_service

    def add_new_car(self, car_data):
        if not car_data:
            raise ExposeException("Car data is missing. Please provide all fields.")

        make = car_data.get('make')
        model = car_data.get('model')
        year = car_data.get('year')
        price = car_data.get('price')

        if not all([make, model, year, price]):
            raise ExposeException("Incomplete car data. Please provide all fields.")

        if not year.isdigit() or not price.isdigit():
            raise ExposeException("Invalid year or price. Please provide a valid number.")


        self.car_service.add_car(make, model, year, price)

    def remove_car(self, id):
        if id is None:
            raise ExposeException("Car id is missing. Please provide a valid id.")

        if not str(id).isdigit():
            raise ExposeException("Invalid car id. Please provide a valid number.")

        self.car_service.remove_car(id)

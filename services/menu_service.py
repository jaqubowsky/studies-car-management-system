class Menu:
    def init_main_menu(self):
        print("\nCar Management System")
        print("1. Add a new car")
        print("2. Remove an existing car")
        print("3. List all cars")
        print("4. Exit")

    def get_add_car_inputs(self):
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        year = input("Enter Year: ")
        price = input("Enter Price: ")
        return make, model, year, price

    def get_remove_car_inputs(self):
        id = input("Enter id of car to remove: ")
        return id


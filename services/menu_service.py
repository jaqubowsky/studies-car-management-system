class MenuService:
    def init_main_menu(self):
        print("\nCar Management System")
        print("1. Add a new car")
        print("2. Remove an existing car")
        print("3. List all cars")
        print("4. Exit")

    def get_add_car_inputs(self):
        try:
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            price = input("Enter Price: ")
            return make, model, int(year), int(price)
        except ValueError:
            print("Invalid data. Please make sure all fields are provided and year and price are numeric.")
            return None

    def get_remove_car_inputs(self):
        try:
            id = input("Enter id of car to remove: ")
            return int(id)
        except ValueError:
            print(f"Invalid id '{id}'. Please provide a numeric value.")
            return None

    def exit_system(self):
        print("Exiting system. Goodbye!")

    def invalid_choice(self):
        print("Invalid choice. Please select a valid option.")

    def get_user_choice(self):
        return input("Choose an option (1-4): ")

    def interrupt_option(self):
        print("Operation interrupted. Returning to main menu.")


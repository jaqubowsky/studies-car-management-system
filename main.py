from services.car_service import CarService
import menu

CHOICES = {
    'NEW_CAR': '1',
    'REMOVE_CAR': '2',
    'LIST_CARS': '3',
    'EXIT': '4'
}

car_service = CarService()

def run_system():
    while True:
        menu.init_main_menu()
        choice = input("Choose an option (1-4): ")

        if choice == CHOICES['NEW_CAR']:
            make, model, year, price = menu.get_add_car_inputs()
            car_service.add_car(make, model, year, price)

        elif choice == CHOICES['REMOVE_CAR']:
            car_service.list_cars()

            index = menu.get_remove_car_inputs()

            car_service.remove_car(index)

        elif choice == CHOICES['LIST_CARS']:
            car_service.list_cars()

        elif choice == CHOICES['EXIT']:
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    run_system()

CHOICES = {
    'NEW_CAR': '1',
    'REMOVE_CAR': '2',
    'LIST_CARS': '3',
    'EXIT': '4'
}

class AppService:
    def __init__(self, car_service, menu_service):
        self.car_service = car_service
        self.menu_service = menu_service

    def add_new_car(self):
        inputs = self.menu_service.get_add_car_inputs()
        if inputs is None:
            return
        make, model, year, price = inputs
        self.car_service.add_car(make, model, year, price)

    def remove_car(self):
        self.car_service.list_cars()
        id = self.menu_service.get_remove_car_inputs()
        if id is None:
            return
        self.car_service.remove_car(id)

    def run_system(self):
        while True:
            self.menu_service.init_main_menu()
            choice = self.menu_service.get_user_choice()

            try:
                if choice == CHOICES['NEW_CAR']:
                    self.add_new_car()

                elif choice == CHOICES['REMOVE_CAR']:
                    self.remove_car()

                elif choice == CHOICES['LIST_CARS']:
                    self.car_service.list_cars()

                elif choice == CHOICES['EXIT']:
                    self.menu_service.exit_system()
                    break

                else:
                    self.menu_service.invalid_choice()

            except KeyboardInterrupt:
                self.menu_service.interrupt_option()
                continue

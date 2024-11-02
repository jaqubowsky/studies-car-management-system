from services.car_service import CarService
from services.menu_service import Menu
from services.app_service import AppService

car_service = CarService()
menu_service = Menu()
app_service = AppService(car_service, menu_service)

if __name__ == "__main__":
    app_service.run_system()

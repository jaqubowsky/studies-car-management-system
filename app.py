import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from services.car_service import CarService
from services.app_service import AppService
from exceptions import ExposeException

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

car_service = CarService()
app_service = AppService(car_service)

@app.route('/')
@app.route('/<car_id>', methods=['GET', 'POST'])
def index(car_id=None):
    if request.method == 'POST':
        car_id = int(car_id)
        app_service.remove_car(car_id)
        flash('Car removed successfully!', 'success')
        return redirect(url_for('index'))

    cars = car_service.get_cars()
    return render_template('index.html', cars=cars)

@app.route('/add-car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        car_data = request.form

        app_service.add_new_car(car_data)
        flash('Car added successfully!', 'success')
        return redirect(url_for('add_car'))
    return render_template('add_car.html')

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, ExposeException):
        flash(str(e), 'error')
    else:
        app.logger.error(f"Unhandled exception: {str(e)}", exc_info=True)
        flash("An unexpected error occurred. Please try again later.", 'error')
    return redirect(url_for('index'))

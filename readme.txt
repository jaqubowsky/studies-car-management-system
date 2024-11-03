# Car Management System

This is a web-based application for managing a collection of cars. It allows users to add, view, and remove cars from the system. The application is built using Flask for the backend and Tailwind CSS for styling.

## Features

- Add new cars with details such as make, model, year, and price.
- View a list of all cars.
- Remove cars from the list.
- User-friendly interface with responsive design.

## Prerequisites

- Python 3.x
- Node.js and npm

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/car-management-system.git
   cd car-management-system
   ```

2. **Set up environment variables:**

   Create a `.env` file in the root directory and add the necessary environment variables. For example:

   ```plaintext
   FLASK_SECRET_KEY=<your-secret-key>
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies:**

   ```bash
   npm install
   ```

5. **Run the application:**

   ```bash
   npm start
   ```

   This will start the Flask server and Tailwind CSS watcher concurrently.

6. **Access the application:**

   Open your web browser and go to `http://localhost:5000`.

## Project Structure

- `app.py`: The main application file containing route definitions and error handling.
- `services/`: Contains service classes for handling business logic.
- `models/`: Contains data models.
- `templates/`: HTML templates for rendering web pages.
- `static/`: Static files including CSS and JavaScript.
- `data/`: JSON file for storing car data.

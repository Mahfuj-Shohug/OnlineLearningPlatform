# Task: Build a Backend System for an Online Learning Platform

This is a Python Django-based online learning platform test project where users can enroll in courses, view course materials, and track their progress.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine: # On Windows

- Python
- pip
- XAMPP (or any other MySQL server)
  - Create a MySQL database named `olp_db`
- Postman or any other API Platform/ or Postman VS extensions

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mahfuj-Shohug/OnlineLearningPlatform.git
    ```

2. Navigate to the project directory:

    ```bash
    cd OnlineLearningPlatform
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv pyenv
    pyenv\Scripts\activate  
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    If you encounter any errors during installation, upgrade pip and try again:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

5. Run database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Load initial data:

    ```bash
    python manage.py loaddata initial_data.json
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and navigate to http://localhost:8000 to access the application where it will be define the all urls for this project.

## Usage URL

- Visit the homepage: (http://localhost:8000) to view the all instraction and api url.
- 


## Some test case here with proper Screenshots

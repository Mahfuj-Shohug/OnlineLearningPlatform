# Online Learning Platform

This is a Django-based online learning platform where users can enroll in courses, view course materials, and track their progress.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python
- pip
- XAMPP (or any other MySQL server)
  - Create a MySQL database named `olp_db`

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
    pyenv\Scripts\activate  # On Windows
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

8. Open your web browser and navigate to http://localhost:8000 to access the application.

## Usage

- Visit the homepage to view available courses and enroll in them.
- Once enrolled, you can access course materials, track your progress, and interact with other learners.
- Use the Django admin interface (http://localhost:8000/admin) to manage courses, enrollments, and other site content.

# StudyBuddy-Django

StudyBuddy-Django is a real-time chat application built using Django. It allows users to communicate in real-time, providing a convenient platform for study groups, collaborative projects, or general conversations.

The project is hosted on Vercel, and the PostgreSQL database is hosted on Railway.

## Features

-   Real-time chat functionality
-   User authentication and registration
-   Creation and management of chat rooms
-   Joining and leaving chat rooms
-   Sending and receiving messages in chat rooms
-   User-friendly interface

## Installation

To run the StudyBuddy-Django project locally, follow these steps:

1. Clone the repository:

    ```shell
    git clone https://github.com/DataRohit/StudyBuddy-Django.git

    ```

2. Change into the project directory:

    ```shell
    cd StudyBuddy-Django

    ```

3. Create and activate a virtual environment (recommended):

    ```
    python3 -m venv myenv
    source myenv/bin/activate  # for Linux/Mac
    myenv\Scripts\activate  # for Windows
    ```

4. Install the dependencies:

    ```shell
    pip install -r requirements.txt

    ```

5. Set up the database:

    - Create a PostgreSQL database (either locally or on a hosting platform like Railway).
    - Update the database configuration in `settings.py` with your database credentials.

6. Apply database migrations:

    ```shell
    python manage.py migrate
    ```

7. Run the development server:

    ```shell
    python manage.py runserver
    ```

8. Open your web browser and navigate to `http://localhost:8000` to access the StudyBuddy-Django application.

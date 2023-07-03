# StudyBuddy-Django

StudyBuddy-Django is a real-time chat application built using Django. It allows users to communicate in real-time, providing a convenient platform for study groups, collaborative projects, or general conversations.

The project is hosted on Vercel, and the PostgreSQL database is hosted on Railway.

This project is based on the work of Dennis Ivy. You can find the original project at [divanov11/StudyBud](https://github.com/divanov11/StudyBud).

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

## Usage

Once you have the StudyBuddy-Django application up and running, follow these steps to use the application:

1. Register a new account or log in with existing credentials.

2. Create a new chat room or join an existing one.

3. Start sending and receiving real-time messages in the chat room.

4. Customize the application as per your requirements or add additional features as needed.

## Technologies Used

The StudyBuddy-Django project utilizes the following technologies:

    - Django: A high-level Python web framework for building web applications.

    - PostgreSQL: A powerful open-source relational database system.

    - Vercel: A cloud platform for static sites and serverless functions.

    - Railway: A hosting platform for databases.

## Contributing

Contributions to StudyBuddy-Django are welcome! If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository.

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

    ```shell
    git checkout -b my-feature
    ```

3. Make your changes and commit them:

    ```shell
    git commit -m "Add my feature"
    ```

4. Push your changes to the branch:

    ```shell
    git push origin my-feature

    ```

5. Open a pull request on the GitHub repository, describing your changes and referencing the related issue (if applicable).

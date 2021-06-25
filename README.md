# dbd_assessment

User authentication API

## To run locally:

- Clone this repo
    ```
    git clone https://github.com/Sirneij/dbd_assessment.git
    ```
- Create a virtual environment
    ```
    virtualenv -p python3.8 env
    ```

- Activate the virtual environment and install dependecies
    ```
    source env/bin/activate
    pip install -r requirements.txt
    ```
- Makemigrations, migrate and runserver

    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
Visit http://localhost:8000

## Main endpoints:

    ```
    /api/auth/login
    /api/auth/register
    /api/auth/logout
    ```
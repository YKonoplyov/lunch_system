# Lunch vote system API

API for voting for your today lunch

## Features

- User registration and authentication.
- Viewing and selecting daily menus.
- Voting for the menu of the day.
- Viewing vote results.
- Admin features to manage restaurants, dishes, and menus.

## Installation

### Requirements:
- Python 3.7+
- Docker
- PostgreSQL (if don`t have Docker)

#### Installation with Docker:
1. Clone repository:
    ```bash
    git clone https://github.com/YKonoplyov/lunch_system.git
    ```
2. Run docker-compose:
    ```bash
    docker-compose up --build
    ```
   
#### Installation without Docker:
1. Clone repository:
    ```bash
    git clone https://github.com/YKonoplyov/lunch_system.git
    ```
2. Create a virtual environment:
    ```shell
   python -m venv venv
   ``` 
   and activate it:
   on windows
   ```shell
   venv\Scripts\activate 
   ```
   on macOS or Linux:
    ```bash
    source venv/bin/activate 
    ```
3. Install the required Python packages:
    ```shell
    pip install -r requirements.txt
    ```
4. Configure the application by setting environment variables:
   DJANGO_SECRET_KEY - secret key for Flask app, you can generate it [here](https://djecrety.ir/)\
   POSTGRES_DB= Your postgres db name
   POSTGRES_HOST=postgres db host
   POSTGRES_USER= postgres db user username
   POSTGRES_PASSWORD= postgres db user password

5. Apply migrations for database:
    ```shell
   python manage.py migrate
    ```
6. Start application:
    ```shell
    python manage.py runserver
    ```

## Documentation

Interactive documentation available at:

- 127.0.0.1/api/doc/swagger/

## API Endpoints

#### Dishes:

- [GET, POST] /api/lunch_service/dishes/: Retrieve a list of all dishes, create dish
- [GET, PUT, PATCH, DELETE] /api/lunch_service/dishes/{id}/: Retrieve, update, patch or delete specific dish by ID.

#### Menus:
- [GET, POST] /api/lunch_service/menus/: Retrieve a list of all menus, create menu.
- [GET, PUT, PATCH, DELETE] /api/lunch_service/menus/{id}/: Retrieve, update, patch or delete specific menu by ID.

#### Restaurants:

- [POST] /api/lunch_service/restaurants/: Create a new restaurant.

#### Tags:

- [POST] /api/lunch_service/tags/: Create a new tag.

#### User Profile:

- [GET, PUT, PATCH] /api/user/me/: Retrieve the authenticated user's profile, update/partially upd. the authenticated user's profile.

- [POST] /api/user/register/: Register a new user.
- [POST] /api/user/token/: Obtain an access token (login).
- [POST] /api/user/token/refresh/: Obtain a refreshed access token.

#### Voting
- [GET] /api/vote_service/results/?date_voted=<YYYY-MM-DD>: Retrieve voting results, if added optional param - date_voted, return voting results for choosen date.
- [POST] /api/vote_service/vote/: Cast a vote.
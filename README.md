# Star Wars API

A RESTful API to fetch, store, and retrieve Star Wars characters, films, and starships in a database, with future voting support. Built with Flask, SQLAlchemy, and PostgreSQL, using Poetry for dependency management.

API is documented with Swagger UI.

## Feature

- Fetch and store Star Wars data from SWAPI
- Retrieve characters, films, and starships with pagination
- Search entities by name
- Save characters, films, and starships
- Full Swagger documentation

## Requirements
- Docker & Docker Compose
- Python 3.11+
- Poetry

## Setup

1. Clone the repository
   ```python
    git clone vote-wars
    ```
3. Install dependencies via Poetry
   ```python
    poetry install
    ```
4. Create a .env file
   ```python
   DATABASE_URL=postgresql+psycopg2://swuser:secretpassword@db:5432/starwars_api
   ```
5. PostgreSQL will be created automatically via docker-compose.yml)
6. ```python
   docker compose up -d api
   ```
7. Apply alembic migration
   ```python
   alembic upgrade head
   ```

## Run the App

To retrieve data from swapi and fill the local database
```python
python scripts/fill_database.py
   ```
or execute 

```python
from actions.actions import store_star_wars_database
store_star_wars_database()
```

To clean up the database 
```python
from scripts.queries import clean_database
clean_database()
```

To start the flask app
```python
poetry run python main.py
```

## API Endpoints

### Fetch data with pagination
- GET /api/characters?page=1&per_page=10
- GET /api/films?page=1&per_page=10
- GET /api/starships?page=1&per_page=10

### Search by name
- GET /api/search/characters?q=luke
- GET /api/search/films?q=hope
- GET /api/search/starships?q=falcon

### Add Data
- POST /api/characters
- POST /api/films
- POST /api/starships

## Swagger 
Available at
```python
http://127.0.0.1:5000/docs
```

## Testing
Runn tests
```python
poetry run pytest --cov=app
```

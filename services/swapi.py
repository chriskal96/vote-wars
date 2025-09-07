import requests

from services.types import SwapiFilm, SwapiPeople, SwapiStarship

# BASE_URL = os.getenv("SWAPI_URL")
BASE_URL = "https://swapi.info/api/"

def get_films():
    url = f"{BASE_URL}/films"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return [SwapiFilm.model_validate(item) for item in data]

def get_people():
    url = f"{BASE_URL}/people"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return [SwapiPeople.model_validate(item) for item in data]

def get_starships():
    url = f"{BASE_URL}/starships"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return [SwapiStarship.model_validate(item) for item in data]
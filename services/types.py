import re

from pydantic import BaseModel, field_validator

def get_id_from_url_validator(resource: str):
    pattern = re.compile(rf"^https://swapi\.info/api/{resource}/(\d+)$")

    def _validator(values):
        ids = []
        for v in values:
            match = pattern.match(v)
            if not match:
                raise ValueError(f"Invalid {resource} URL format: {v}")
            ids.append(int(match.group(1)))
        return ids

    return _validator

class SwapiFilm(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    url: str
    characters: list[int]
    starships: list[int]

    _validate_characters = field_validator("characters", mode="before")(get_id_from_url_validator("people"))
    _validate_starships = field_validator("starships", mode="before")(get_id_from_url_validator("starships"))



class SwapiPeople(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    height : str
    mass : str
    url: str
    films: list[int]
    starships: list[int]

    _validate_films = field_validator("films", mode="before")(get_id_from_url_validator("films"))
    _validate_starships = field_validator("starships", mode="before")(get_id_from_url_validator("starships"))



class SwapiStarship(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed:str
    crew: str
    passengers: str
    cargo_capacity:str
    consumables:str
    hyperdrive_rating:str
    MGLT:str
    starship_class: str
    url: str
    films: list[int]

    _validate_films = field_validator("films", mode="before")(get_id_from_url_validator("films"))


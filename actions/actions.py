import datetime
import uuid

from sqlalchemy.exc import IntegrityError

from database import SessionLocal
from models import Character, Starship, Film
from services.swapi import get_people, get_starships, get_films


def save_characters(db, characters):
    """ Save characters to the database and return a mapping of swapi_id to Character instances. """
    character_to_link={}
    if not characters:
        return character_to_link
    for c in characters:
        character = Character(
            id=uuid.uuid4(),
            name=c.name,
            mass=c.mass,
            hair_color=c.hair_color,
            eye_color=c.eye_color,
            birth_year=c.birth_year,
            height=c.height,
            gender=c.gender,
            swapi_id=int(c.url.split("/")[-1]),
            created_at=datetime.datetime.now(),
            modified_at=datetime.datetime.now(),
        )
        try:
            db.add(character)
            db.commit()
            character_to_link[character.swapi_id] = character
        except IntegrityError:
            db.rollback()
            print(f"Character already exists, skipping: name= {character.name}, id= {character.swapi_id}")
            continue
    return character_to_link

def save_starships(db,starships):
    """ Save starships to the database and return a mapping of swapi_id to Starship instances. """
    starship_to_link = {}
    if not starships:
        return starship_to_link
    for s in starships:
        starship = Starship(
            id=uuid.uuid4(),
            name=s.name,
            model=s.model,
            manufacturer=s.manufacturer,
            cost_in_credits=s.cost_in_credits,
            length=s.length,
            max_atmosphering_speed=s.max_atmosphering_speed,
            crew=s.crew,
            passengers=s.passengers,
            cargo_capacity=s.cargo_capacity,
            consumables=s.consumables,
            hyperdrive_rating=s.hyperdrive_rating,
            MGLT=s.MGLT,
            starship_class=s.starship_class,
            swapi_id=int(s.url.split("/")[-1]),
            created_at=datetime.datetime.now(),
            modified_at=datetime.datetime.now(),
        )
        try:
            db.add(starship)
            db.commit()
            starship_to_link[starship.swapi_id] = starship
        except IntegrityError:
            db.rollback()
            print(f"Starship already exists, skipping: name= {starship.name}, id= {starship.swapi_id}")
            continue
    return starship_to_link

def save_films(db,films, characters_to_link, starships_to_link):
    """ Save films to the database and link characters and starships. """
    films_to_link = {}
    if not films:
        return films_to_link
    for f in films:
        film = Film(
            id=uuid.uuid4(),
            title=f.title,
            episode_id=f.episode_id,
            director=f.director,
            producer=f.producer,
            opening_crawl=f.opening_crawl,
            swapi_id=int(f.url.split("/")[-1]),
            release_date=datetime.datetime.strptime(f.release_date, "%Y-%m-%d") if f.release_date else None,
            created_at=datetime.datetime.now(),
            modified_at=datetime.datetime.now(),
        )
        try:
            # Link characters
            for c in f.characters:
                character = characters_to_link.get(c)
                if character:
                    film.characters.append(character)

            # Link starships
            for ship in f.starships:
                starship = starships_to_link.get(ship)
                if starship:
                    film.starships.append(starship)
            db.add(film)
            db.commit()
            films_to_link[film.swapi_id] = film
        except IntegrityError:
            db.rollback()
            print(f"Film already exists, skipping: title= {film.title}, id= {film.swapi_id}")
            continue
    return films_to_link

def link_characters_starships(db, characters, characters_to_link, ships_to_link):
    """ Link characters to their starships. """
    for c in characters:
        character = characters_to_link.get(int(c.url.split("/")[-1]))
        for ship_id in c.starships:
            starship = ships_to_link.get(ship_id)
            if starship and starship not in character.starships:
                character.starships.append(starship)
    db.commit()

def store_star_wars_database():
    """ Fetch data from SWAPI and store it in the local database."""
    db = SessionLocal()

    characters = get_people()
    starships = get_starships()
    films = get_films()

    try:
        characters_to_link = save_characters(db, characters)
        ships_to_link = save_starships(db, starships)
        save_films(db,films,characters_to_link, ships_to_link)
        link_characters_starships(db,characters, characters_to_link, ships_to_link)
    finally:
        db.close()

def create_character(data:dict):
    """ Create a new character in the database."""
    db = SessionLocal()
    try:
        character = Character(
            id=uuid.uuid4(),
            name=data.get('name'),
            mass=data.get('mass'),
            hair_color=data.get('hair_color'),
            eye_color=data.get('eye_color'),
            birth_year=data.get('birth_year'),
            gender=data.get('gender'),
            height=data.get('height'),
            swapi_id=data.get('swapi_id'),
            created_at = datetime.datetime.now(),
            modified_at = datetime.datetime.now()

        )
        db.add(character)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError(f"Character with name '{character.name}' or swapi_id '{character.swapi_id}' already exists.")
    finally:
        db.close()
    return character

def create_film(data:dict):
    """ Create a new film in the database."""
    db = SessionLocal()
    try:
        film = Film(
            id=uuid.uuid4(),
            title=data.get('title'),
            episode_id=data.get('episode_id'),
            director=data.get('director'),
            producer=data.get('producer'),
            opening_crawl=data.get('opening_crawl'),
            swapi_id=data.get('swapi_id'),
            release_date=datetime.datetime.strptime(data.get('release_date'), "%Y-%m-%d") if data.get('release_date') else None,
            created_at = datetime.datetime.now(),
            modified_at = datetime.datetime.now()

        )
        db.add(film)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError(f"Film with title '{film.title}' or swapi_id '{film.swapi_id}' already exists.")
    finally:
        db.close()
    return film

def create_starship(data:dict):
    """ Create a new starship in the database."""
    db = SessionLocal()
    try:
        starship = Starship(
            id=uuid.uuid4(),
            name=data.get('name'),
            model=data.get('model'),
            manufacturer=data.get('manufacturer'),
            cost_in_credits=data.get('cost_in_credits'),
            length=data.get('length'),
            max_atmosphering_speed=data.get('max_atmosphering_speed'),
            crew=data.get('crew'),
            passengers=data.get('passengers'),
            cargo_capacity=data.get('cargo_capacity'),
            consumables=data.get('consumables'),
            hyperdrive_rating=data.get('hyperdrive_rating'),
            MGLT=data.get('MGLT'),
            starship_class=data.get('starship_class'),
            swapi_id=data.get('swapi_id'),
            created_at = datetime.datetime.now(),
            modified_at = datetime.datetime.now()

        )
        db.add(starship)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError(f"Starship with name '{starship.name}' or swapi_id '{starship.swapi_id}' already exists.")
    finally:
        db.close()
    return starship
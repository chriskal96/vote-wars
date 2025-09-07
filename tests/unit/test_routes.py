import datetime
import json
import random
import uuid
from http import HTTPStatus
from unittest.mock import Mock

from sqlalchemy.exc import OperationalError

from models import Character, Film, Starship


class TestCharactersResource:
    def test_get_characters(self,client,monkeypatch):
        name="Bruce Wayne"
        id_ = uuid.uuid4()
        character = Character(
            id=id_,
            name=name,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.character.CharacterRepository.get_all', Mock(return_value=[character]))
        response = client.get("/api/v1/vote_wars/characters?page=1&per_page=10")
        assert response.status_code == HTTPStatus.OK
        data = response.get_json()
        assert "characters" in data
        assert data["total"] == 1
        assert data['characters'][0]['name'] == name
        assert data['characters'][0]['id'] == str(id_)

    def test_get_character_by_name(self,client,monkeypatch):
        name="Bruce Wayne"
        id_ = uuid.uuid4()
        character = Character(
            id=id_,
            name=name,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.character.CharacterRepository.get_by_name', Mock(return_value=character))
        response = client.get("/api/v1/vote_wars/characters?name=Bruce%20Wayne")
        assert response.status_code == HTTPStatus.OK
        data = response.get_json()
        assert "characters" in data
        assert data["total"] == 1
        assert data['characters'][0]['name'] == name
        assert data['characters'][0]['id'] == str(id_)

    def test_should_return_not_found(self,client,monkeypatch):
        name="Bruce Wayne"
        id_ = uuid.uuid4()
        character = Character(
            id=id_,
            name=name,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.character.CharacterRepository.get_by_name', Mock(return_value=character))
        response = client.get("/api/v1/vote_wars/characterinoss?name=Bruce%20Wayne")
        assert response.status_code == HTTPStatus.NOT_FOUND


    def test_create_character(self,client):
        payload = {
            "name": f"TestCharacter_{random.randint(1000, 9999)}",
            "birth_year": "19BBY",
            "gender": "male",
            "hair_color": "black",
            "eye_color": "blue",
            "height": "172",
            "mass": "77",
            "swapi_id": random.randint(1000, 9999)

        }
        response = client.post(
            "/api/v1/vote_wars/characters",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.CREATED

    def test_should_raise_character_exists(self,client,monkeypatch):
        payload = {
            "name": f"TestCharacter_{random.randint(1000, 9999)}",
            "birth_year": "19BBY",
            "gender": "male",
            "hair_color": "black",
            "eye_color": "blue",
            "height": "172",
            "mass": "77",
            "swapi_id": random.randint(1000, 9999)

        }
        monkeypatch.setattr('api.swapi.create_character', Mock(side_effect=ValueError("Character already exists")))
        response = client.post(
            "/api/v1/vote_wars/characters",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_should_raise_internal_error(self,client,monkeypatch):
        payload = {
            "name": f"TestCharacter_{random.randint(1000, 9999)}",
            "birth_year": "19BBY",
            "gender": "male",
            "hair_color": "black",
            "eye_color": "blue",
            "height": "172",
            "mass": "77",
            "swapi_id": random.randint(1000, 9999)

        }
        monkeypatch.setattr('api.swapi.create_character', Mock(side_effect=OperationalError))
        response = client.post(
            "/api/v1/vote_wars/characters",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

class TestFilmsResource:
    def test_get_films(self,client,monkeypatch):
        title="Star Wars"
        id_ = uuid.uuid4()
        film = Film(
            id=id_,
            title=title,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.film.FilmRepository.get_all', Mock(return_value=[film]))
        response = client.get("/api/v1/vote_wars/films?page=1&per_page=10")
        assert response.status_code == HTTPStatus.OK
        data = response.get_json()
        assert "films" in data
        assert data["total"] == 1
        assert data['films'][0]['title'] == title
        assert data['films'][0]['id'] == str(id_)

    def test_get_film_by_name(self,client,monkeypatch):
        title="Star Wars"
        id_ = uuid.uuid4()
        film = Film(
            id=id_,
            title=title,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.film.FilmRepository.get_by_name', Mock(return_value=film))
        response = client.get("/api/v1/vote_wars/films?name=Star%20Wars")
        assert response.status_code == HTTPStatus.OK
        data = response.get_json()
        assert "films" in data
        assert data["total"] == 1
        assert data['films'][0]['title'] == title
        assert data['films'][0]['id'] == str(id_)

    def test_should_return_not_found(self,client,monkeypatch):
        title="Star Wars"
        id_ = uuid.uuid4()
        film = Film(
            id=id_,
            title=title,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.film.FilmRepository.get_by_name', Mock(return_value=film))
        response = client.get("/api/v1/vote_wars/filmind?name=Star%20Wars")
        assert response.status_code == HTTPStatus.NOT_FOUND


    def test_create_film(self,client):
        payload = {
            "title": f"TestFilm_{random.randint(1000, 9999)}",
            "swapi_id": random.randint(1000, 9999)

        }
        response = client.post(
            "/api/v1/vote_wars/films",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.CREATED

    def test_should_raise_film_exists(self,client,monkeypatch):
        payload = {
            "title": f"TestFilm_{random.randint(1000, 9999)}",
            "swapi_id": random.randint(1000, 9999)

        }
        monkeypatch.setattr('api.swapi.create_film', Mock(side_effect=ValueError("Film already exists")))
        response = client.post(
            "/api/v1/vote_wars/characters",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_should_raise_internal_error(self,client,monkeypatch):
        payload = {
            "title": f"TestFilm_{random.randint(1000, 9999)}",
            "swapi_id": random.randint(1000, 9999)

        }
        monkeypatch.setattr('api.swapi.create_film', Mock(side_effect=OperationalError))
        response = client.post(
            "/api/v1/vote_wars/films",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

class TestStarshipsResource:
    def test_get_starships(self,client,monkeypatch):
        name="Batmobile"
        id_ = uuid.uuid4()
        starship = Starship(
            id=id_,
            name=name,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.starship.StarshipRepository.get_all', Mock(return_value=[starship]))
        response = client.get("/api/v1/vote_wars/starships?page=1&per_page=10")
        assert response.status_code == HTTPStatus.OK
        data = response.get_json()
        assert "starships" in data
        assert data["total"] == 1
        assert data['starships'][0]['name'] == name
        assert data['starships'][0]['id'] == str(id_)

    def test_get_starship_by_name(self,client,monkeypatch):
        name="Batmobile"
        id_ = uuid.uuid4()
        starship = Starship(
            id=id_,
            name=name,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.starship.StarshipRepository.get_by_name', Mock(return_value=starship))
        response = client.get("/api/v1/vote_wars/starships?name=Batmobile")
        assert response.status_code == HTTPStatus.OK
        data = response.get_json()
        assert "starships" in data
        assert data["total"] == 1
        assert data['starships'][0]['name'] == name
        assert data['starships'][0]['id'] == str(id_)

    def test_should_return_not_found(self,client,monkeypatch):
        name="Batmobile"
        id_ = uuid.uuid4()
        starship = Starship(
            id=id_,
            name=name,
            swapi_id=11,

        )
        monkeypatch.setattr('repositories.starship.StarshipRepository.get_by_name', Mock(return_value=starship))
        response = client.get("/api/v1/vote_wars/starshipss?name=Batmobile")
        assert response.status_code == HTTPStatus.NOT_FOUND


    def test_create_starship(self,client):
        payload = {
            "name": f"TestStarship_{random.randint(1000, 9999)}",
            "swapi_id": random.randint(1000, 9999)

        }
        response = client.post(
            "/api/v1/vote_wars/starships",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.CREATED

    def test_should_raise_starship_exists(self,client,monkeypatch):
        payload = {
            "name": f"TestStarship_{random.randint(1000, 9999)}",
            "swapi_id": random.randint(1000, 9999)

        }
        monkeypatch.setattr('api.swapi.create_starship', Mock(side_effect=ValueError("Starship already exists")))
        response = client.post(
            "/api/v1/vote_wars/starships",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_should_raise_internal_error(self,client,monkeypatch):
        payload = {
            "name": f"TestStarship_{random.randint(1000, 9999)}",
            "swapi_id": random.randint(1000, 9999)

        }
        monkeypatch.setattr('api.swapi.create_starship', Mock(side_effect=OperationalError))
        response = client.post(
            "/api/v1/vote_wars/starships",
            data=json.dumps(payload),
            content_type="application/json"
        )
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

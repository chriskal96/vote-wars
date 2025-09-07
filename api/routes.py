from http import HTTPStatus

from flask import request, Response
from flask_restx import  Resource

from actions.actions import create_character, create_starship, create_film
from api.schemas import characters_list_model, films_list_model, starships_list_model, ns, character_model, film_model, \
    starship_model
from database import get_db
from repositories.character import CharacterRepository
from repositories.film import FilmRepository
from repositories.starship import StarshipRepository

@ns.route('/characters')
class CharactersResource(Resource):
    @ns.doc(description="Retrieve Star Wars characters with pagination or by name")
    @ns.doc(params={
        'name': 'Optional. Name to search',
        'page': 'Page number (default 1)',
        'per_page': 'Items per page (default 10)'
    })
    @ns.marshal_with(characters_list_model)
    def get(self):
        """Get Star Wars characters."""

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        name = request.args.get('name', None)

        db = next(get_db())
        char_repo = CharacterRepository(db)
        if name:
            characters = char_repo.get_by_name(
                name=name,
            )
            total=1 if characters else 0
        else:
            characters = char_repo.get_all(
                offset=(page - 1) * per_page,
                limit=per_page
            )
            total = len(characters) if characters else 0

        return {
            'characters': characters,
            'total': total,
            'page': page,
            'per_page': per_page
        }
    @ns.doc(description="Create a new Star Wars character")
    @ns.expect(character_model, validate=True)
    def post(self):
        """Create a Star Wars character."""
        data = request.get_json()
        try:
            create_character(data)
        except ValueError as e:
            ns.abort(HTTPStatus.BAD_REQUEST, str(e))
        except Exception as e:
            ns.abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(e))
        return Response(status=HTTPStatus.CREATED)

@ns.route('/films')
class FilmsResource(Resource):
    @ns.doc(description="Retrieve Star Wars films with pagination or by name")
    @ns.doc(params={
        'name': 'Optional. Name to search',
        'page': 'Page number (default 1)',
        'per_page': 'Items per page (default 10)'
    })
    @ns.marshal_with(films_list_model)
    def get(self):
        """Get Star Wars films."""

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        name = request.args.get('name', None)

        db = next(get_db())
        char_repo = FilmRepository(db)
        if name:
            films = char_repo.get_by_name(
                name=name,
            )
            total=1 if films else 0
        else:
            films = char_repo.get_all(
                offset=(page - 1) * per_page,
                limit=per_page
            )
            total = len(films)
        return {
            'films': films,
            'total': total,
            'page': page,
            'per_page': per_page
        }, HTTPStatus.OK

    @ns.doc(description="Create a new Star Wars film")
    @ns.expect(film_model, validate=True)
    def post(self):
        """Create a Star Wars film."""
        data = request.get_json()
        try:
            create_film(data)
        except ValueError as e:
            ns.abort(HTTPStatus.BAD_REQUEST, str(e))
        except Exception as e:
            ns.abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(e))
        return Response(status=HTTPStatus.CREATED)

@ns.route('/starships')
class StarshipsResource(Resource):
    @ns.doc(description="Retrieve Star Wars starships with pagination or by name")
    @ns.doc(params={
        'name': 'Optional. Name to search',
        'page': 'Page number (default 1)',
        'per_page': 'Items per page (default 10)'
    })
    @ns.marshal_with(starships_list_model)
    def get(self):
        """Get Star Wars starships."""

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        name = request.args.get('name', None)

        db = next(get_db())
        starship_repo = StarshipRepository(db)
        if name:
            starships = starship_repo.get_by_name(
                name=name,
            )
            total=1 if starships else 0
        else:
            starships = starship_repo.get_all(
                offset=(page - 1) * per_page,
                limit=per_page
            )
            total = len(starships)
        return {
            'starships': starships,
            'total': total,
            'page': page,
            'per_page': per_page
        }, HTTPStatus.OK

    @ns.doc(description="Create a new Star Wars starship")
    @ns.expect(starship_model, validate=True)
    def post(self):
        """Create a Star Wars starship."""
        data = request.get_json()
        try:
            create_starship(data)
        except ValueError as e:
            ns.abort(HTTPStatus.BAD_REQUEST, str(e))
        except Exception as e:
            ns.abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(e))
        return Response(status=HTTPStatus.CREATED)

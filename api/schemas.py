from flask_restx import fields, Namespace

ns = Namespace('vote_wars', description='Star Wars character operations')

character_model = ns.model('Character', {
    'id': fields.String(required=False, description='Character ID'),
    'name': fields.String(required=True, description='Character name'),
    'birth_year': fields.String(required=False, description='Birth year of the character'),
    'gender': fields.String(required=False, description = 'Gender of the character'),
    'hair_color': fields.String(required=False, description='Hair color of the character'),
    'eye_color': fields.String(required=False, description='Eye color of the character'),
    'height': fields.String(required=False, description='Height of the character'),
    'mass': fields.String(required=False, description='Mass of the character'),
    'swapi_id': fields.Integer(required=False, description='SWAPI ID of the character'),
    'created_at': fields.String(required=False, description='Creation timestamp'),
    'modified_at': fields.String(required=False, description='Last modified timestamp'),
    'vote_count': fields.Integer(required=False, description='Vote count for the character')
})

characters_list_model = ns.model('CharactersList', {
    'characters': fields.List(fields.Nested(character_model), required=True, description='List of characters'),
    'total': fields.Integer(required=True, description='Total number of characters returned'),
    'page': fields.Integer(required=True, description='Current page number'),
    'per_page': fields.Integer(required=True, description='Number of items per page')
})


film_model = ns.model('Film', {
    'id': fields.String(required=False, description='Film ID'),
    'title': fields.String(required=True, description='Film title'),
    'episode_id': fields.Integer(required=False, description='Episode ID of the film'),
    'director': fields.String(required=False, description='Director of the film'),
    'producer': fields.String(required=False, description='Producer of the film'),
    'opening_crawl': fields.String(required=False, description='Opening crawl text of the film'),
    'swapi_id': fields.Integer(required=False, description='SWAPI ID of the film'),
    'release_date': fields.String(required=False, description='Release date of the film'),
    'created_at': fields.String(required=False, description='Creation timestamp'),
    'modified_at': fields.String(required=False, description='Last modified timestamp'),
    'vote_count': fields.Integer(required=False, description='Vote count for the film')

})

films_list_model = ns.model('FilmsList', {
    'films': fields.List(fields.Nested(film_model), required=True, description='List of films'),
    'total': fields.Integer(required=True, description='Total number of films returned'),
    'page': fields.Integer(required=True, description='Current page number'),
    'per_page': fields.Integer(required=True, description='Number of items per page')
})

starship_model = ns.model('Starship', {
    'id': fields.String(required=False, description='Starship ID'),
    'name': fields.String(required=True, description='Starship name'),
    'model': fields.String(required=False, description='Model of the starship'),
    'manufacturer': fields.String(required=False, description='Manufacturer of the starship'),
    'cost_in_credits': fields.String(required=False, description='Cost in credits of the starship'),
    'length': fields.String(required=False, description='Length of the starship'),
    'max_atmosphering_speed': fields.String(required=False, description='Max atmosphering speed of the starship'),
    'crew': fields.String(required=False, description='Crew size of the starship'),
    'passengers': fields.String(required=False, description='Passenger capacity of the starship'),
    'cargo_capacity': fields.String(required=False, description='Cargo capacity of the starship'),
    'consumables': fields.String(required=False, description='Consumables of the starship'),
    'hyperdrive_rating': fields.String(required=False, description='Hyperdrive rating of the starship'),
    'MGLT': fields.String(required=False, description='MGLT of the starship'),
    'starship_class': fields.String(required=False, description='Class of the starship'),
    'swapi_id': fields.Integer(required=False, description='SWAPI ID of the starship'),
    'created_at': fields.String(required=False, description='Creation timestamp'),
    'modified_at': fields.String(required=False, description='Last modified timestamp'),
    'vote_count': fields.Integer(required=False, description='Vote count for the starship')

})

starships_list_model = ns.model('StarshipsList', {
    'starships': fields.List(fields.Nested(starship_model), required=True, description='List of starships'),
    'total': fields.Integer(required=True, description='Total number of starships returned'),
    'page': fields.Integer(required=True, description='Current page number'),
    'per_page': fields.Integer(required=True, description='Number of items per page')
})

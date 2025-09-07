from sqlalchemy import Column, Integer, ForeignKey, UUID, Table
from database import Base


character_film = Table(
    "character_film",
    Base.metadata,
    Column("character_id", UUID, ForeignKey("characters.id"), primary_key=True),
    Column("film_id", UUID, ForeignKey("films.id"), primary_key=True),
)
character_starship = Table(
    "character_starship",
    Base.metadata,
    Column("character_id", UUID, ForeignKey("characters.id"), primary_key=True),
    Column("starship_id", UUID, ForeignKey("starships.id"), primary_key=True),
)

film_starship = Table(
    "starship_film",
    Base.metadata,
    Column("starship_id", UUID,ForeignKey("starships.id"), primary_key=True),
    Column("film_id", UUID,ForeignKey("films.id"), primary_key=True)
)
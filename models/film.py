from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import relationship
from database import Base

character_film_association = Table(
    "character_film",
    Base.metadata,
    Column("character_id", Integer, primary_key=True),
    Column("film_id", Integer, primary_key=True)
)

starship_film_association = Table(
    "starship_film",
    Base.metadata,
    Column("starship_id", Integer, primary_key=True),
    Column("film_id", Integer, primary_key=True)
)

class Film(Base):
    __tablename__ = "film"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    director = Column(String, nullable=True)
    producer = Column(String, nullable=True)
    release_date = Column(String, nullable=True)

    # Relationships with characters and starships
    characters = relationship("Character", secondary=character_film_association, back_populates="films")
    starships = relationship("Starship", secondary=starship_film_association, back_populates="films")

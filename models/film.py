from sqlalchemy import Column, Integer, String, UUID, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from models.associations import film_starship
from models.character import character_film



class Film(Base):
    __tablename__ = "films"
    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    episode_id = Column(Integer, nullable=True)
    director = Column(String, nullable=True)
    producer = Column(String, nullable=True)
    opening_crawl = Column(Text, nullable=True)
    swapi_id = Column(Integer, index=True, unique=True,nullable=False)
    release_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    modified_at = Column(DateTime, nullable=True)
    vote_count = Column(Integer, default=0)

    characters = relationship("Character", secondary=character_film, back_populates="films")
    starships = relationship("Starship", secondary=film_starship, back_populates="films")
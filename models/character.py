from sqlalchemy import Column, Integer, String, UUID, DateTime
from sqlalchemy.orm import relationship
from database import Base
from models.associations import character_film, character_starship


class Character(Base):
    __tablename__ = "characters"
    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    birth_year = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    hair_color = Column(String, nullable=True)
    eye_color = Column(String, nullable=True)
    height = Column(String, nullable=True)
    mass = Column(String, nullable=True)
    swapi_id = Column(Integer, index=True, unique=True,nullable=False)
    created_at = Column(DateTime, nullable=True)
    modified_at = Column(DateTime, nullable=True)
    vote_count = Column(Integer, default=0)

    films = relationship("Film", secondary=character_film, back_populates="characters")
    starships = relationship("Starship", secondary=character_starship, back_populates="pilots")

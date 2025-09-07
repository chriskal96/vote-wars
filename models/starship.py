from sqlalchemy import Column, Integer, String, UUID, DateTime
from sqlalchemy.orm import relationship
from database import Base
from models.associations import character_starship, film_starship


class Starship(Base):
    __tablename__ = "starships"
    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    model = Column(String, nullable=True)
    manufacturer = Column(String, nullable=True)
    cost_in_credits = Column(String, nullable=True)
    length = Column(String, nullable=True)
    max_atmosphering_speed = Column(String, nullable=True)
    crew = Column(String, nullable=True)
    passengers = Column(String, nullable=True)
    cargo_capacity = Column(String, nullable=True)
    consumables = Column(String, nullable=True)
    hyperdrive_rating = Column(String, nullable=True)
    MGLT = Column(String, nullable=True)
    starship_class = Column(String, nullable=True)
    swapi_id = Column(Integer, index=True, unique=True,nullable=False)
    created_at = Column(DateTime, nullable=True)
    modified_at = Column(DateTime, nullable=True)
    vote_count = Column(Integer, default=0)

    pilots = relationship("Character", secondary=character_starship, back_populates="starships")
    films = relationship("Film", secondary=film_starship, back_populates="starships")

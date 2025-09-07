from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.film import character_film_association


class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    height = Column(String, nullable=True)
    mass = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    birth_year = Column(String, nullable=True)

    # Films relationship
    films = relationship("Film", secondary=character_film_association, back_populates="characters")

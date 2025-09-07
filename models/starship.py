from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.film import starship_film_association


class Starship(Base):
    __tablename__ = "starship"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    model = Column(String, nullable=True)
    manufacturer = Column(String, nullable=True)
    cost_in_credits = Column(String, nullable=True)
    length = Column(String, nullable=True)
    crew = Column(String, nullable=True)
    passengers = Column(String, nullable=True)
    starship_class = Column(String, nullable=True)

    # Films relationship
    films = relationship("Film", secondary=starship_film_association, back_populates="starships")

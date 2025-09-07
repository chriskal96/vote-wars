
from sqlalchemy.orm import Session
from models import Film

class FilmRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, offset=0, limit=10):
        return self.db.query(Film).offset(offset).limit(limit).all()

    def get_by_name(self,name):
        return self.db.query(Film).filter(Film.name.ilike(f"%{name}%")).one_or_none()


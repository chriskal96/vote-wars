
from sqlalchemy.orm import Session
from models import Character

class CharacterRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, offset=0, limit=10):
        return self.db.query(Character).offset(offset).limit(limit).all()


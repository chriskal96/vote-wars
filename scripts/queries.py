from sqlalchemy import text
from database import SessionLocal


def clean_database():
    db = SessionLocal()

    try:
        # Association tables first
        db.execute(text('TRUNCATE TABLE starship_film RESTART IDENTITY CASCADE;'))
        db.execute(text('TRUNCATE TABLE character_film RESTART IDENTITY CASCADE;'))
        db.execute(text('TRUNCATE TABLE character_starship RESTART IDENTITY CASCADE;'))

        # Main tables
        db.execute(text('TRUNCATE TABLE characters RESTART IDENTITY CASCADE;'))
        db.execute(text('TRUNCATE TABLE films RESTART IDENTITY CASCADE;'))
        db.execute(text('TRUNCATE TABLE starships RESTART IDENTITY CASCADE;'))

        db.commit()
        print('All data removed.')
    finally:
        db.close()
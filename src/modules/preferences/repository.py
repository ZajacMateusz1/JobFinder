from sqlalchemy.orm import Session


class PreferencesRepository:
    def __init__(self, db: Session):
        self.db = db

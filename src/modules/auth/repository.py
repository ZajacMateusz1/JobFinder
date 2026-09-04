from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.db.models.user import User
from src.db.models.preferences import Preferences
from .exceptions import UserAlreadyExistsError


class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(
        self,
        username: str,
        hashed_password: str,
        email: str,
    ) -> dict:
        new_user = User(username=username, hashed_password=hashed_password, email=email)
        self.db.add(new_user)
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise UserAlreadyExistsError()
        self.db.refresh(new_user)
        return {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
        }

    def get_user_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        return self.db.scalar(stmt)

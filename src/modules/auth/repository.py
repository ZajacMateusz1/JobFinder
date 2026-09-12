from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.db.models import User
from .exceptions import UserAlreadyExistsError


class AuthRepository:
    def __init__(self, db: Session):
        self._db = db

    def create_user(
        self,
        username: str,
        hashed_password: str,
        email: str,
    ) -> dict:
        user = User(username=username, hashed_password=hashed_password, email=email)
        self._db.add(user)
        try:
            self._db.commit()
        except IntegrityError:
            self._db.rollback()
            raise UserAlreadyExistsError()
        self._db.refresh(user)
        return user

    def get_user_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        return self._db.scalar(stmt)

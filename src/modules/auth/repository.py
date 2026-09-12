from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.db.models import User
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
        user = User(username=username, hashed_password=hashed_password, email=email)
        self.db.add(user)
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise UserAlreadyExistsError()
        self.db.refresh(user)
        return user

    def get_user_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        return self.db.scalar(stmt)

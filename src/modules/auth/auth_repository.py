from sqlalchemy.orm import Session
from src.db.models.user import User
from src.db.models.preferences import Preferences


class AuthRepository:
    def create_user(
        self, username: str, hashed_password: str, email: str, db: Session
    ) -> dict:
        new_user = User(username=username, hashed_password=hashed_password, email=email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
        }

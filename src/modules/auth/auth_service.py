from fastapi import HTTPException
import jwt
from datetime import datetime, timedelta, timezone

from .auth_repository import AuthRepository
from .auth_utils import hash_password, verify_password
from .auth_schemas import RegisterRequest


class AuthService:
    def __init__(
        self,
        auth_repository: AuthRepository,
        secret_key: str,
        jwt_algorithm: str = "HS256",
    ):
        self.auth_repository = auth_repository
        self.secret_key = secret_key
        self.jwt_algorithm = jwt_algorithm

    def register_user(self, user: RegisterRequest) -> dict:
        hashed_password = hash_password(user.password)
        return self.auth_repository.create_user(
            user.username,
            hashed_password,
            user.email,
        )

    def authenticate_user(self, username: str, password: str) -> dict:
        user = self.auth_repository.get_user_by_username(username)
        if not user:
            raise HTTPException(
                status_code=401, detail="Username or password incorrect"
            )
        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=401, detail="Username or password incorrect"
            )
        refresh_token = self._generate_token(user.id, user.username, True)
        access_token = self._generate_token(user.id, user.username)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "id": user.id,
            "username": user.username,
        }

    def _generate_token(
        self,
        id: str,
        username: str,
        isRefresh: bool = False,
    ) -> str:
        payload = {
            "sub": id,
            "username": username,
            "exp": (
                datetime.now(timezone.utc) + timedelta(days=7)
                if isRefresh
                else datetime.now(timezone.utc) + timedelta(minutes=15)
            ),
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.jwt_algorithm)

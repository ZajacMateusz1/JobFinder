import jwt
from datetime import datetime, timedelta, timezone

from .repository import AuthRepository
from .utils import hash_password, verify_password, validate_jwt_payload
from .schemas import RegisterRequest
from .exceptions import InvalidCredentialsError


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
            raise InvalidCredentialsError()
        if not verify_password(password, user.hashed_password):
            raise InvalidCredentialsError()
        refresh_token = self._generate_token(user.id, user.username, True)
        access_token = self._generate_token(user.id, user.username)

        return {
            "refresh_token": refresh_token,
            "response": {
                "access_token": access_token,
                "id": user.id,
                "username": user.username,
            },
        }

    def refresh_access_token(self, refresh_token: str | None) -> dict:
        if not refresh_token:
            raise InvalidCredentialsError()
        try:
            decoded = jwt.decode(refresh_token, self.secret_key, self.jwt_algorithm)
        except jwt.PyJWTError:
            raise InvalidCredentialsError()
        payload = validate_jwt_payload(decoded)
        if payload.get("type") != "refresh":
            raise InvalidCredentialsError()
        new_access_token = self._generate_token(payload["sub"], payload["username"])
        return {"access_token": new_access_token}

    def _generate_token(
        self,
        id: str | int,
        username: str,
        isRefresh: bool = False,
    ) -> str:
        now = datetime.now(timezone.utc)
        token_type = "refresh" if isRefresh else "access"
        expire = now + timedelta(days=7) if isRefresh else now + timedelta(minutes=15)
        payload = {
            "sub": str(id),
            "username": username,
            "type": token_type,
            "exp": expire,
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.jwt_algorithm)

import jwt
from datetime import datetime, timedelta, timezone

from .repository import AuthRepository
from .utils import hash_password, verify_password, validate_jwt_payload
from .schemas import RegisterRequest
from .exceptions import InvalidCredentialsError, InvalidJwtTokenError


class AuthService:
    def __init__(
        self,
        auth_repository: AuthRepository,
        secret_key: str,
        jwt_algorithm: str,
    ):
        self.auth_repository = auth_repository
        self.secret_key = secret_key
        self.jwt_algorithm = jwt_algorithm

    def register_user(self, user: RegisterRequest) -> dict:
        hashed_password = hash_password(user.password)
        create_user_response = self.auth_repository.create_user(
            user.username,
            hashed_password,
            user.email,
        )
        refresh_token = self._generate_token(
            create_user_response["id"], create_user_response["username"], True
        )
        access_token = self._generate_token(
            create_user_response["id"], create_user_response["username"]
        )
        create_user_response["access_token"] = access_token
        return {"refresh_token": refresh_token, "response": create_user_response}

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
                "token_type": "bearer",
                "id": user.id,
                "username": user.username,
            },
        }

    def refresh_access_token(self, refresh_token: str | None) -> dict:
        if not refresh_token:
            raise InvalidJwtTokenError()
        try:
            decoded = jwt.decode(
                jwt=refresh_token, key=self.secret_key, algorithms=[self.jwt_algorithm]
            )
        except jwt.PyJWTError:
            raise InvalidJwtTokenError()
        payload = validate_jwt_payload(decoded)
        if payload.type != "refresh":
            raise InvalidJwtTokenError()
        new_access_token = self._generate_token(payload.sub, payload.username)
        return {"access_token": new_access_token}

    def _generate_token(
        self,
        id: str | int,
        username: str,
        is_refresh: bool = False,
    ) -> str:
        now = datetime.now(timezone.utc)
        token_type = "refresh" if is_refresh else "access"
        expire = now + timedelta(days=7) if is_refresh else now + timedelta(minutes=15)
        payload = {
            "sub": str(id),
            "username": username,
            "type": token_type,
            "exp": expire,
        }
        return jwt.encode(
            payload=payload, key=self.secret_key, algorithm=self.jwt_algorithm
        )

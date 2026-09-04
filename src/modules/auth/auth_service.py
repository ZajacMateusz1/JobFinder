import jwt
from sqlalchemy.orm import Session

from .auth_repository import AuthRepository
from .auth_utils import hash_password, verify_password
from .auth_schemas import RegisterRequest, LoginRequest


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

    def register_user(self, user: RegisterRequest, db: Session) -> dict:
        hashed_password = hash_password(user.password)
        return self.auth_repository.create_user(
            user.username, hashed_password, user.email, db
        )

    def authenticate_user(self, username: str, password: str) -> bool:
        pass

    def _generate_token(self, payload: dict) -> str:
        return jwt.encode(payload, self.secret_key, algorithm=self.jwt_algorithm)

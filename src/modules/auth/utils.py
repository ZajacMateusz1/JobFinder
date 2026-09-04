from passlib.context import CryptContext
from .schemas import JwtTokenPayload
from .exceptions import InvalidCredentialsError

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def validate_jwt_payload(payload: dict):
    try:
        return JwtTokenPayload.model_validate(payload)
    except ValueError:
        raise InvalidCredentialsError()

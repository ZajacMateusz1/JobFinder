from typing import Annotated

from fastapi import Depends
import jwt
from fastapi.security import OAuth2PasswordBearer

from src.config.env import settings
from .service import AuthService
from .repository import AuthRepository
from src.db.connection import db_dependency
from .utils import validate_jwt_payload
from .schemas import JwtTokenPayload
from .exceptions import InvalidJwtTokenError


def get_auth_service(db: db_dependency) -> AuthService:
    auth_repository = AuthRepository(db)
    return AuthService(auth_repository, settings.secret_key, settings.jwt_algorithm)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> JwtTokenPayload:
    try:
        decoded = jwt.decode(
            jwt=token, key=settings.secret_key, algorithms=[settings.jwt_algorithm]
        )
    except jwt.PyJWTError:
        raise InvalidJwtTokenError()
    payload = validate_jwt_payload(decoded)
    if payload.type != "access":
        raise InvalidJwtTokenError()
    return payload


auth_service_dependency = Annotated[AuthService, Depends(get_auth_service)]
current_user_dependency = Annotated[JwtTokenPayload, Depends(get_current_user)]

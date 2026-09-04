from typing import Annotated

from fastapi import Depends

from src.config.env import settings
from .auth_service import AuthService
from .auth_repository import AuthRepository
from src.db.connection import db_dependency


def get_auth_service(db: db_dependency) -> AuthService:
    auth_repository = AuthRepository(db)
    return AuthService(auth_repository, settings.secret_key)


auth_service_dependency = Annotated[AuthService, Depends(get_auth_service)]

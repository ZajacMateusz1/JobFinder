from typing import Annotated

from fastapi import Depends

from src.config.env import settings
from .auth_service import AuthService
from .auth_repository import AuthRepository


def get_auth_service() -> AuthService:
    auth_repository = AuthRepository()
    return AuthService(auth_repository, settings.secret_key)


auth_service_dependency = Annotated[AuthService, Depends(get_auth_service)]

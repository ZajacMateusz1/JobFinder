from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from src.db.connection import db_dependency
from .auth_dependencies import get_auth_service
from .auth_service import AuthService
from .auth_schemas import RegisterRequest, LoginRequest, RegisterResponse

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register", status_code=201, response_model=RegisterResponse)
def register(
    user: RegisterRequest,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
    db: db_dependency,
):
    return auth_service.register_user(user, db)


@auth_router.post("/login")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    pass

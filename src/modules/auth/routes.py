from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from .dependencies import get_auth_service
from .service import AuthService
from .schemas import RegisterRequest, RegisterResponse, LoginResponse, RefreshResponse

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register", status_code=201, response_model=RegisterResponse)
def register(
    user: RegisterRequest,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    return auth_service.register_user(user)


@auth_router.post("/login", response_model=LoginResponse)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
    response: Response,
):
    login_data = auth_service.authenticate_user(form_data.username, form_data.password)
    response.set_cookie(
        key="refresh_token",
        value=login_data["refresh_token"],
        httponly=True,
    )
    return login_data["response"]


@auth_router.post("/refresh", response_model=RefreshResponse)
def refresh(
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    pass

from fastapi import APIRouter, Depends, Response, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from .dependencies import auth_service_dependency
from .schemas import RegisterRequest, RegisterResponse, LoginResponse, RefreshResponse

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register", status_code=201, response_model=RegisterResponse)
def register(
    user: RegisterRequest, auth_service: auth_service_dependency, response: Response
):
    register_data = auth_service.register_user(user)
    response.set_cookie(
        key="refresh_token", value=register_data["refresh_token"], httponly=True
    )
    return register_data["response"]


@auth_router.post("/login", response_model=LoginResponse)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: auth_service_dependency,
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
    auth_service: auth_service_dependency,
    refresh_token: Annotated[str | None, Cookie()],
):
    return auth_service.refresh_access_token(refresh_token)

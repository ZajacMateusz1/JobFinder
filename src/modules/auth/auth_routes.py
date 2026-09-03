from fastapi import APIRouter

from src.modules.auth.auth_schemas import RegisterRequest, LoginRequest

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register")
async def register(user: RegisterRequest):
    pass


@auth_router.post("/login")
async def login(user: LoginRequest):
    pass

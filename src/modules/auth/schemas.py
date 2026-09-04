from pydantic import BaseModel, Field, EmailStr
from typing import Literal
from datetime import datetime


class RegisterRequest(BaseModel):
    username: str = Field(min_length=1, max_length=100, description="Username")
    password: str = Field(min_length=8, max_length=100, description="Password")
    email: EmailStr = Field(description="Email", max_length=100)


class RegisterResponse(BaseModel):
    username: str
    email: EmailStr


class LoginResponse(BaseModel):
    access_token: str
    id: int
    username: str


class RefreshResponse(BaseModel):
    access_token: str


class JwtTokenPayload(BaseModel):
    sub: str
    username: str
    type: Literal["refresh", "access"]
    exp: datetime

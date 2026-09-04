from pydantic import BaseModel, Field, EmailStr


class LoginRequest(BaseModel):
    username: str = Field(min_length=1, max_length=100, description="Username")
    password: str = Field(min_length=8, max_length=100, description="Password")


class RegisterRequest(LoginRequest):
    email: EmailStr = Field(description="Email")


class RegisterResponse(BaseModel):
    username: str
    email: EmailStr

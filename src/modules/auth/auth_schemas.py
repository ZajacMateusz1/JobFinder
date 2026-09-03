from pydantic import BaseModel, Field, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr = Field(description="Email")
    password: str = Field(min_length=8, max_length=100, description="Password")


class RegisterRequest(LoginRequest):
    username: str = Field(min_length=1, max_length=100, description="Username")

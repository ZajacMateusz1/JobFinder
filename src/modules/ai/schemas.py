from typing import Literal
from decimal import Decimal
from pydantic import BaseModel, Field
from enum import StrEnum


class Skill(StrEnum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    JAVA = "java"
    CSHARP = "cs#"
    CPP = "cpp"
    RUBY = "ruby"
    PHP = "php"
    SWIFT = "swift"
    KOTLIN = "kotlin"
    GO = "go"
    RUST = "rust"
    TYPESCRIPT = "typescript"
    HTML = "html"
    CSS = "css"
    REACT = "react"
    ANGULAR = "angular"
    VUEJS = "vuejs"
    DJANGO = "django"
    FLASK = "flask"
    FASTAPI = "fastapi"
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    MONGODB = "mongodb"
    MOONGOOSE = "mongoose"


class AnalyzeCvAiResponse(BaseModel):
    location: str | None = Field(min_length=1, default=None)
    skills: list[Skill]
    min_salary: Decimal | None = Field(default=None)
    max_salary: Decimal | None = Field(default=None)
    remote_work: bool | None = Field(default=None)
    experience_level: Literal["intern", "junior", "mid", "senior", "lead"] | None = (
        Field(default=None)
    )

from typing import Literal
from decimal import Decimal
from pydantic import BaseModel, Field


class AnalyzeCvResponse(BaseModel):
    location: str | None = Field(min_length=1, default=None)
    skills: list[str]
    min_salary: Decimal | None = Field(default=None)
    max_salary: Decimal | None = Field(default=None)
    remote_work: bool | None = Field(default=None)
    experience_level: Literal["intern", "junior", "mid", "senior", "lead"] | None = (
        Field(default=None)
    )

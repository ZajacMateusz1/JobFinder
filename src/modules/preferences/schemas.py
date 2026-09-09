from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class AnalyzeCvResponse(BaseModel):
    id: int
    location: str | None
    min_salary: Decimal | None
    max_salary: Decimal | None
    remote_work: bool | None
    experience_level: str | None
    user_id: int

    model_config = ConfigDict(from_attributes=True)

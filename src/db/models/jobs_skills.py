from sqlalchemy import ForeignKey, Column, Table
from src.db.connection import Base

jobs_skills = Table(
    "jobs_skills",
    Base.metadata,
    Column("jobs_id", ForeignKey("jobs.id"), primary_key=True),
    Column("skills_id", ForeignKey("skills.id"), primary_key=True),
)

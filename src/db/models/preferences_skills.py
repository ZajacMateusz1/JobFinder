from sqlalchemy import ForeignKey, Column, Table
from src.db.connection import Base

preferences_skills = Table(
    "preferences_skills",
    Base.metadata,
    Column("preferences_id", ForeignKey("preferences.id"), primary_key=True),
    Column("skills_id", ForeignKey("skills.id"), primary_key=True),
)

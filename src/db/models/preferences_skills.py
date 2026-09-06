from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.connection import Base


class PreferencesSkills(Base):
    __tablename__ = "preferences_skills"

    preferences_id: Mapped[int] = mapped_column(
        ForeignKey("preferences.id"), primary_key=True
    )
    skills_id: Mapped[int] = mapped_column(ForeignKey("skills.id"), primary_key=True)
    preferences: Mapped["Preferences"] = relationship(
        back_populates="preferences_skills"
    )
    skills: Mapped["Skills"] = relationship(back_populates="preferences_skills")

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.connection import Base


class Skills(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    preferences_skills: Mapped[list["PreferencesSkills"]] = relationship(
        back_populates="skills"
    )

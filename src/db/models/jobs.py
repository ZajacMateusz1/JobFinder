from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.connection import Base
from datetime import datetime


class Jobs(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    company: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    posted_at: Mapped[datetime] = mapped_column(nullable=False)
    expire_at: Mapped[datetime] = mapped_column(nullable=False)
    salary: Mapped[str | None] = mapped_column(default=None)
    skills: Mapped[list["Skills"]] = relationship(
        secondary="jobs_skills", back_populates="jobs"
    )

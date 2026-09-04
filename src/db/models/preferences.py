from decimal import Decimal
from sqlalchemy import ForeignKey, String, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.connection import Base


class Preferences(Base):
    __tablename__ = "preferences"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    min_salary: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 2), nullable=True)
    max_salary: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 2), nullable=True)
    remote_work: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), unique=True, nullable=False
    )
    user: Mapped["User"] = relationship(back_populates="preferences")

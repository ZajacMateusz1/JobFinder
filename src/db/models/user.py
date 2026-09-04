from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.connection import Base
from src.db.models.preferences import Preferences


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    preferences: Mapped[Preferences] = relationship(
        back_populates="user_id", uselist=False
    )

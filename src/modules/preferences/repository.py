from sqlalchemy import select
from sqlalchemy.orm import Session
from src.modules.ai.schemas import AnalyzeCvAiResponse
from src.db.models import Preferences, Skills
from .schemas import PreferencesRequest
from .exceptions import UserPreferencesNotFoundError


class PreferencesRepository:
    def __init__(self, db: Session):
        self._db = db

    def save_preferences(
        self,
        preferences_data: AnalyzeCvAiResponse | PreferencesRequest,
        user_id: str,
    ):
        stmt = select(Skills).where(Skills.name.in_(preferences_data.skills))
        skills = self._db.scalars(stmt).all()
        preferences = Preferences(
            location=preferences_data.location,
            min_salary=preferences_data.min_salary,
            max_salary=preferences_data.max_salary,
            remote_work=preferences_data.remote_work,
            user_id=int(user_id),
            skills=skills,
            experience_level=preferences_data.experience_level,
        )
        self._db.add(preferences)
        self._db.commit()
        self._db.refresh(preferences)
        return preferences

    def change_preferences(self, new_preferences: PreferencesRequest, user_id: str):
        stmt = select(Preferences).where(Preferences.user_id == int(user_id))
        preferences = self._db.scalar(stmt)
        if preferences is None:
            raise UserPreferencesNotFoundError()
        data = new_preferences.model_dump(exclude_unset=True)
        if "skills" in data:
            stmt = select(Skills).where(Skills.name.in_(data["skills"]))
            skills = self._db.scalars(stmt).all()
            preferences.skills = skills
        for key, value in data.items():
            if key != "skills":
                preferences.__setattr__(key, value)
        self._db.commit()
        self._db.refresh(preferences)
        return preferences

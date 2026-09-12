from sqlalchemy.orm import Session
from src.modules.ai.schemas import AnalyzeCvAiResponse
from src.db.models import Preferences
from .schemas import PreferencesRequest


class PreferencesRepository:
    def __init__(self, db: Session):
        self._db = db

    def save_preferences(
        self,
        preferences_data: AnalyzeCvAiResponse | PreferencesRequest,
        user_id: str,
    ):
        preferences = Preferences(
            location=preferences_data.location,
            min_salary=preferences_data.min_salary,
            max_salary=preferences_data.max_salary,
            remote_work=preferences_data.remote_work,
            user_id=int(user_id),
            skills=preferences_data.skills,
            experience_level=preferences_data.experience_level,
        )
        self._db.add(preferences)
        self._db.commit()
        self._db.refresh()
        return preferences

    def change_preferences(self, new_preferences: PreferencesRequest, user_id: str):
        pass

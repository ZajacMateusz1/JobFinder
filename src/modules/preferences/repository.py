from sqlalchemy import select
from sqlalchemy.orm import Session
from src.modules.ai.schemas import AnalyzeCvAiResponse
from src.db.models.preferences import Preferences
from src.db.models.preferences_skills import PreferencesSkills
from src.db.models.skills import Skills
from .schemas import CreatePreferencesRequest


class PreferencesRepository:
    def __init__(self, db: Session):
        self._db = db

    def save_preferences(
        self,
        preferences_data: AnalyzeCvAiResponse | CreatePreferencesRequest,
        user_id: str,
    ):
        preferences = Preferences(
            location=preferences_data.location,
            min_salary=preferences_data.min_salary,
            max_salary=preferences_data.max_salary,
            remote_work=preferences_data.remote_work,
            user_id=int(user_id),
            experience_level=preferences_data.experience_level,
        )
        self._db.add(preferences)
        self._db.flush()
        find_skills_stmt = select(Skills.id).where(
            Skills.name.in_(preferences_data.skills)
        )
        skills = [
            PreferencesSkills(skills_id=skill_id, preferences_id=preferences.id)
            for skill_id in self._db.scalars(find_skills_stmt)
        ]
        self._db.add_all(skills)
        self._db.commit()
        return preferences

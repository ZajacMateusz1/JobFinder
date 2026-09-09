from sqlalchemy import select
from sqlalchemy.orm import Session
from src.modules.ai.schemas import AnalyzeCvAiResponse
from src.db.models.preferences import Preferences
from src.db.models.preferences_skills import PreferencesSkills
from src.db.models.skills import Skills


class PreferencesRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_preferences(self, ai_result: AnalyzeCvAiResponse, user_id: str):
        preferences = Preferences(
            location=ai_result.location,
            min_salary=ai_result.min_salary,
            max_salary=ai_result.max_salary,
            remote_work=ai_result.remote_work,
            user_id=int(user_id),
            experience_level=ai_result.experience_level,
        )
        self.db.add(preferences)
        self.db.flush()
        find_skills_stmt = select(Skills.id).where(Skills.name.in_(ai_result.skills))
        skills = [
            PreferencesSkills(skills_id=skill_id, preferences_id=preferences.id)
            for skill_id in self.db.scalars(find_skills_stmt)
        ]
        self.db.add_all(skills)
        self.db.commit()
        return preferences

from fastapi import UploadFile
from .repository import PreferencesRepository
from src.modules.ai.service import AiService
from .utils import validate_cv_file
from .schemas import PreferencesRequest


class PreferencesService:
    def __init__(self, repository: PreferencesRepository, ai_service: AiService):
        self._repository = repository
        self._ai_service = ai_service

    async def analyze_cv(self, cv_file: UploadFile, user_id: str):
        validate_cv_file(cv_file=cv_file)
        cv_content = await cv_file.read()
        ai_result = self._ai_service.analyze_cv(cv_content=cv_content)
        analyze_cv_response = self._repository.save_preferences(
            preferences_data=ai_result, user_id=user_id
        )
        return analyze_cv_response

    def create_preferences(self, preferences: PreferencesRequest, user_id: str):
        create_preferences_response = self._repository.save_preferences(
            preferences, user_id
        )
        return create_preferences_response

    def change_preferences(self, new_preferences: PreferencesRequest, user_id: str):
        change_preferences_response = self._repository.change_preferences(
            new_preferences=new_preferences, user_id=user_id
        )
        return change_preferences_response

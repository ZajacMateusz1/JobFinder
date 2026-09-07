from fastapi import UploadFile
from .repository import PreferencesRepository
from src.modules.ai.service import AiService
from .utils import validate_cv_file


class PreferencesService:
    def __init__(self, repository: PreferencesRepository, ai_service: AiService):
        self.repository = repository
        self.ai_service = ai_service

    async def analyze_cv(self, cv_file: UploadFile):
        validate_cv_file(cv_file=cv_file)
        cv_content = await cv_file.read()
        result_cv = self.ai_service.analyze_cv(cv_content=cv_content)
        print(result_cv)

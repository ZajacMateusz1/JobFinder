from fastapi import Depends
from typing import Annotated

from src.db.connection import db_dependency
from .repository import PreferencesRepository
from .service import PreferencesService
from src.modules.ai.dependencies import ai_service_dependecy


def get_preferences_service(
    db: db_dependency, ai_service: ai_service_dependecy
) -> PreferencesService:
    preferences_repository = PreferencesRepository(db)
    return PreferencesService(preferences_repository, ai_service=ai_service)


preferences_service_dependency = Annotated[
    PreferencesService, Depends(get_preferences_service)
]

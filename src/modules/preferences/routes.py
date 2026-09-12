from fastapi import APIRouter, UploadFile

from src.modules.auth.dependencies import current_user_dependency
from .schemas import PreferencesResponse, CreatePreferencesRequest
from .dependencies import preferences_service_dependency

preferences_router = APIRouter(prefix="/preferences", tags=["preferences"])


@preferences_router.post("/analyze_cv", response_model=PreferencesResponse)
async def analyze_cv(
    cv_file: UploadFile,
    preferences_service: preferences_service_dependency,
    current_user: current_user_dependency,
):
    return await preferences_service.analyze_cv(
        cv_file=cv_file, user_id=current_user.sub
    )


@preferences_router.post("", response_model=PreferencesResponse)
def create_preferences(
    preferences: CreatePreferencesRequest,
    preferences_service: preferences_service_dependency,
    current_user: current_user_dependency,
):
    return preferences_service.create_preferences(
        preferences=preferences, user_id=current_user.sub
    )

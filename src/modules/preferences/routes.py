from fastapi import APIRouter, UploadFile

from src.modules.auth.dependencies import current_user_dependency
from .schemas import AnalyzeCvResponse
from .dependencies import preferences_service_dependency

preferences_router = APIRouter()


@preferences_router.post("/analyze_cv", response_model=AnalyzeCvResponse)
async def analyze_cv(
    cv_file: UploadFile,
    preferences_service: preferences_service_dependency,
    current_user: current_user_dependency,
):
    return await preferences_service.analyze_cv(
        cv_file=cv_file, user_id=current_user.sub
    )

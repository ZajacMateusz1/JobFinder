from fastapi import APIRouter, UploadFile

from .dependencies import preferences_service_dependency

preferences_router = APIRouter()


@preferences_router.post("/analyze_cv")
async def analyze_cv(
    cv_file: UploadFile, preferences_service: preferences_service_dependency
):
    return await preferences_service.analyze_cv(cv_file=cv_file)

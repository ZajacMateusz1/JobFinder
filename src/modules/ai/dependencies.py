from typing import Annotated
from fastapi import Depends

from .providers.base import AIProvider
from .service import AiService
from .providers.gemini import GeminiProvider
from src.config.env import settings


def get_ai_service() -> AiService:
    ai_provider = GeminiProvider(settings.gemini_api_key)
    return AiService(ai_provider)


ai_service_dependecy = Annotated[AiService, Depends(get_ai_service)]

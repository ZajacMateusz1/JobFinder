from .providers.base import AIProvider
from .schemas import AnalyzeCvResponse


class AiService:
    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider

    def analyze_cv(self, cv_content: bytes) -> AnalyzeCvResponse:
        ai_response = self.ai_provider.analyze_cv(cv_content)
        return AnalyzeCvResponse.model_validate(ai_response)

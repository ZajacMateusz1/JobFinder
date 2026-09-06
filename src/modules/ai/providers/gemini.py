from google import genai
from google.genai import types
from .base import AIProvider
from ..schemas import AnalyzeCvResponse


class GeminiProvider(AIProvider):
    def __init__(self, gemini_api_key):
        self.client = genai.Client(api_key=gemini_api_key)

    def analyze_cv(self, cv_content):
        prompt = "Summarize this document"
        interaction = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[
                types.Part.from_bytes(
                    data=cv_content,
                    mime_type="application/pdf",
                ),
                prompt,
            ],
        )
        print(interaction.text)

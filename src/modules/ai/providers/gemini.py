from google import genai
from google.genai import types
from .base import AIProvider
from ..schemas import AnalyzeCvResponse


class GeminiProvider(AIProvider):
    def __init__(self, gemini_api_key):
        self.client = genai.Client(api_key=gemini_api_key)

    def analyze_cv(self, cv_content):
        prompt = """
            Analyze this CV and extract:

            - candidate location
            - minimum salary expectation, if explicitly stated
            - maximum salary expectation, if explicitly stated
            - whether the candidate prefers/accepts remote work
            - technical and professional skills
            - overall experience level

            For experience_level use exactly one of:
            - intern: internship/student with little or no professional experience
            - junior: entry-level professional
            - mid: intermediate professional
            - senior: experienced professional with substantial expertise
            - lead: senior professional who leads projects, teams, or technical direction

            Do not invent information that is not present in the CV.
            """

        interaction = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[
                types.Part.from_bytes(
                    data=cv_content,
                    mime_type="application/pdf",
                ),
                prompt,
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json", response_schema=AnalyzeCvResponse
            ),
        )
        return interaction.parsed

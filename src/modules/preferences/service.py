from .repository import PreferencesRepository


class PreferencesService:
    def __init__(self, repository: PreferencesRepository):
        self.repository = repository

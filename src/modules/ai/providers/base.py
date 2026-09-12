from abc import ABC, abstractmethod


class AIProvider(ABC):
    @abstractmethod
    def analyze_cv(self, cv_content: bytes):
        pass

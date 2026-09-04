from src.exceptions.app_exception import AppException


class InvalidCredentialsError(AppException):
    def __init__(self):
        super().__init__(status_code=401, message="Invalid username or password")

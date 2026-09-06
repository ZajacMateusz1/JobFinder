from src.exceptions.app_exception import AppException


class InvalidCVFileError(AppException):
    def __init__(self):
        super().__init__(
            status_code=400,
            message="Invalid CV file format. Please upload a valid CV file.",
        )


class InvalidFileSizeError(AppException):
    def __init__(self):
        super().__init__(
            status_code=413,
            message="Invalid file size.",
        )

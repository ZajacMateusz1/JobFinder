class AppException(Exception):
    def __init__(
        self,
        status_code: int = 500,
        message: str = "Internal Server Error",
    ):
        super().__init__(message)
        self.status_code = status_code

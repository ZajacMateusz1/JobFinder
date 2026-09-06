from fastapi import UploadFile

from src.modules.preferences.exceptions import InvalidCVFileError, InvalidFileSizeError

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


def validate_cv_file(cv_file: UploadFile):
    if cv_file.size is None or cv_file.size > MAX_FILE_SIZE:
        raise InvalidFileSizeError()
    if cv_file.content_type != "application/pdf":
        raise InvalidCVFileError()

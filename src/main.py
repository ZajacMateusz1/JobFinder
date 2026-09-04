from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from modules.auth.routes import auth_router
from exceptions.app_exception import AppException

app = FastAPI()


@app.get("/api/health")
def health_check():
    return {"message": "ok"}


app.include_router(auth_router, prefix="/api")


@app.exception_handler(AppException)
def exception_handler(request: Request, exception: AppException):
    return JSONResponse(
        status_code=exception.status_code, content={"detail": str(exception)}
    )

from fastapi import FastAPI

from src.modules.auth.auth_routes import auth_router

app = FastAPI()


@app.get("/api/health")
def health_check():
    return {"message": "ok"}


app.include_router(auth_router, prefix="/api")

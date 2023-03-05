from fastapi import FastAPI

from src.api.router import health


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(health.health_router)
    return app

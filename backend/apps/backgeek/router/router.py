from fastapi import FastAPI
from fastapi import APIRouter


def init_router() -> FastAPI:
    app = FastAPI()
    router = APIRouter()

    app.include_router(router, prefix="/api")

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    return app

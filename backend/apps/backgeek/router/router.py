from fastapi import FastAPI
from .item_crud.create import router


def init_router() -> FastAPI:
    app = FastAPI()

    app.include_router(router, prefix="/api")

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    return app

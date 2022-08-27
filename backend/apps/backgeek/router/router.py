from fastapi import FastAPI
from .item_crud.create import router

app = FastAPI()
app.include_router(router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Hello World"}
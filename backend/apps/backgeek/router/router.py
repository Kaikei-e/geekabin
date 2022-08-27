from fastapi import FastAPI, Response, status

from .item_crud.create import router

app = FastAPI()
app.include_router(router, prefix="/api")


@app.get("/")
def read_root():
    return Response(status_code=status.HTTP_200_OK, content={"message": "Hello World"})

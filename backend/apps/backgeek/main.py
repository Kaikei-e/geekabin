import uvicorn

from router.router import app


@app.get("/")
async def root():
    return {"message": "Hello World"}


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=9020, reload=True)


if __name__ == "__main__":
    main()

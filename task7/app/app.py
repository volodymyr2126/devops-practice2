import os

from fastapi import FastAPI

app = FastAPI()
app_name = os.getenv("APP_NAME", "FastAPI")


@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": f"Hello from {app_name}!"}

import logging

from fastapi import FastAPI

app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/healthz")
async def healthz():
    return {"message": "OK"}


@app.get("/greet_user")
async def greet_user(name: str):
    return {"message": f"Hello, {name}"}
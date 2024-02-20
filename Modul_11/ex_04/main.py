from fastapi import FastAPI

from src.routes import todos

app = FastAPI()

app.include_router(todos.router, prefix="/api")


@app.get("/")
def index():
    return {"message": "Todo Application"}

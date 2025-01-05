from fastapi import FastAPI
from .routers import task
from .routers import user

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to TaskManager"}

app.include_router(user.user)
app.include_router(task.task)

# Start command: python -m uvicorn app.main:app

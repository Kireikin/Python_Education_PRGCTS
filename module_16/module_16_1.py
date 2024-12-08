from fastapi import FastAPI
from pydantic import BaseModel  # для POST-запроса — добавление данных

app = FastAPI()  # Создаем экземпляр приложения FastAPI


class Item(BaseModel):  # POST-запрос — добавление данных
    username: str
    age: int


@app.get("/")  # Определение базового маршрута
async def root():
    return {"message": "Главная страница"}


@app.get("/user/admin")  # Определение входа администратора
async def get_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_id(user_id: int) -> dict:
    return {"Вы вошли как пользователь №": user_id}


@app.get("/user/{username}/{age}")
async def get_user(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username} , Возраст: {age}"}

# START COMMAND IN LOCAL TERMINAL: uvicorn module_16_1:app --reload

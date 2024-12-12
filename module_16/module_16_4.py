from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel  # для POST-запроса — добавление данных
from typing import Annotated

app = FastAPI()  # Создаем экземпляр приложения FastAPI


class User(BaseModel):  # POST-запрос — добавление данных
    id: int
    username: str
    age: int


# БД пользователей (словарь):
users = []


@app.get("/")  # Определение базового маршрута
async def root():
    return {"message": "Домашнее задание по теме: 'Модели данных Pydantic'/n Цель: научиться описывать "
                       "и использовать Pydantic модель."}


@app.get("/user/admin")  # Определение входа администратора
async def get_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")  # модифицируем согласно заданию на валидацию
async def log_in_from_user_id(user_id: Annotated[int, Path(ge=1, le=100,
                                                           title="User ID",
                                                           description="Enter User ID, "
                                                                       "The ID must be a positive integer 1 to 100",
                                                           example=5
                                                           )]):
    return {"Вы вошли как пользователь №": user_id}


@app.get("/user/{username}/{age}")
async def check_user_data(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      regex="^[a-zA-Z0-9_-]+$",
                                      title="User ID",
                                      description="Enter the user's name, the name must consist of letters and/or "
                                                  "numbers and contain at least 5 and no more than 20 characters",
                                      example="UrbanUser"
                                      )],

        age: Annotated[int, Path(ge=18, le=120,
                                 title="User age",
                                 description="Enter age, the age must be a positive integer 18 to 120",
                                 example=24
                                 )]
):
    return {"message": f"Информация о пользователе. Имя: {username} , Возраст: {age}"}


@app.get("/users")
async def show_me_all_users():
    return users


@app.post("/user/{username}/{age}")  # регистрировать нового пользователя
async def add_new_user(username: str, age: int):
    new_id = max(user["id"] for user in users) + 1 if users else 1
    new_user = {"id": new_id, "username": username, "age": {age}}
    users.append(new_user)
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")  # меняем имя и возраст (данные) пользователя (записи) по id
async def update_user_data(user_id: int, username: str, age: int):
    for user_ in users:
        if user_["id"] == user_id:
            user_["username"] = username
            user_["age"] = age
            return users
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user_from_id(user_id: int):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return {"detail": "Пользователь удален"}
    raise HTTPException(status_code=404, detail="User was not found")

# START COMMAND IN LOCAL TERMINAL: uvicorn module_16_4:app --reload

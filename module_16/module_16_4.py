from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel  # для POST-запроса — добавление данных
from typing import Annotated

app = FastAPI()  # Создаем экземпляр приложения FastAPI


class Users(BaseModel):  # POST-запрос — добавление данных
    id: int
    user_id: int
    username: str
    age: int


# БД пользователей (словарь):
users = [{"id": 1, "name": "Имя", "age": 18}]


@app.get("/")  # Определение базового маршрута
async def root():
    return {"message": "Домашнее задание по теме 'CRUD Запросы': Get, Post, Put Delete."}


@app.get("/user/admin")  # Определение входа администратора
async def get_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")  # модифицируем согласно заданию на валидацию
async def get_user_id(user_id: Annotated[int, Path(ge=1, le=100,
                                                   title="User ID",
                                                   description="Enter User ID, "
                                                               "The ID must be a positive integer 1 to 100",
                                                   example=5
                                                   )]):
    return {"Вы вошли как пользователь №": user_id}


@app.get("/user/{username}/{age}")
async def get_user(
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
async def get_users():
    return users


@app.post("/user/{username}/{age}")  # Создать новую задачу
async def post_user(username: str, age: int):
    new_id = max(user["id"] for user in users) + 1 if users else 1
    new_user = {"id": new_id, "username": username, "age": {age}}
    users.append(new_user)
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")  # меняем имя и возраст (данные) пользователя (записи) по id
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user["id"] == user_id:
            user["username"] = username
            user["age"] = age
            return user
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return {"detail": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")

# START COMMAND IN LOCAL TERMINAL: uvicorn module_16_4:app --reload

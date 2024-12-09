from fastapi import FastAPI, Path
from pydantic import BaseModel  # для POST-запроса — добавление данных
from typing import Annotated

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

# START COMMAND IN LOCAL TERMINAL: uvicorn module_16_2:app --reload

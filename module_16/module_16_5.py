from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel  # для POST-запроса — добавление данных
from typing import Annotated, List


# Создаем экземпляр приложения FastAPI:
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")


class User(BaseModel):  # POST-запрос — добавление данных
    id: int
    username: str
    age: int


# БД пользователей (словарь):
users: List[User] = [
   User(id=1, username="UrbanUser", age=24),
   User(id=2, username="UrbanTest", age=22),
   User(id=3, username="Capybara", age=60)
]


@app.get("/", response_class=HTMLResponse)
async def get_all_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_task(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}", response_class=HTMLResponse)  # регистрировать нового пользователя
async def add_new_user(
        #  reguest: Request,
        username: Annotated[str, Path(min_length=3, max_length=100)],
        age: Annotated[int, Path(ge=12, le=120)]
):
    new_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": Request, "users": users})


@app.put("/user/{user_id}/{username}/{age}", response_class=HTMLResponse)  # меняем имя и возраст (данные)
# пользователя (записи) по id
async def update_user_data(
        # reguest: Request,
        user_id: Annotated[int, Path(ge=1)],
        username: Annotated[str, Path(min_length=3, max_length=100)],
        age: Annotated[int, Path(ge=12, le=120)]
):
    for user_ in users:
        if user_.id == user_id:
            user_.username = username
            user_.age = age
            return templates.TemplateResponse("users.html", {"request": Request, "users": users})
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_class=HTMLResponse)
async def delete_user_from_id(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return templates.TemplateResponse("users.html", {"request": request, "users": users})
    raise HTTPException(status_code=404, detail="User was not found")

# START COMMAND IN LOCAL TERMINAL: uvicorn module_16_5:app --reload

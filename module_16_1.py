from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user")
async def user_id(username: str, age: int):
    return f"Информация о пользователе. Имя:{username}, Возраст:{age}"


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> str:
    return f"Вы вошли как пользователь: {user_id}"


@app.get("/user/admin")
async def user():
    return "Вы вошли как администратор"

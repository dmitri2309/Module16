from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user")
async def user_id(username: str, age: int):
    #return ("message": "Информация о пользователе.", "Имя":{username} "age":{age})
    return {"Информация о пользователе. Имя":{username}, "Возраст":{age}}


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"Вы вошли как пользователь": {user_id}}

@app.get("/user/admin")
async def user():
    return {"message": "Вы вошли как адмистратор"}




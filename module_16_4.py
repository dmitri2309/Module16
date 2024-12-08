from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


# GET /users
@app.get("/users", response_model=List[User])
def get_users():
    return users


# POST /user/{username}/{age}
@app.post("/user/{username}/{age}", response_model=User)
def create_user(
        username: str = Path(..., min_length=5, max_length=20, description="Enter username", example="UrbanUser"),
        age: int = Path(..., ge=18, le=120, description="Enter age", example=24)
):
    new_id = len(users) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# PUT /user/{user_id}/{username}/{age}
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(
        user_id: int,
        username: str = Path(..., min_length=5, max_length=20, description="Enter username"),
        age: int = Path(..., ge=18, le=120, description="Enter age")
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# DELETE /user/{user_id}
@app.delete("/user/{user_id}", response_model=dict)
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {'detail': f'User with ID {user_id} has been deleted'}
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} was not found.")


@app.delete("/")
def kill_users():
    users.clear()

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI KT",
    description="This is a test FastAPI application.",
    version="1.0.0"
)

stored_user = None


class User(BaseModel):
    name: str
    age: int
    password: str


class UserResponse(BaseModel):
    name: str
    age: int


@app.post("/user")
def create_user(data: User):
    global stored_user
    stored_user = data
    return {"message": "User created successfully"}


@app.get("/user/{name}", response_model=UserResponse)
def get_user(name: str):
    if stored_user and stored_user.name == name:
        return stored_user
    return {"message": "User not found"}
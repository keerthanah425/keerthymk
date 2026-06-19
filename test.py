from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI(
    title="FastAPI KT",
    description="This is a test FastAPI application.",
    version="1.0.0"
)

def verify_token(token: str = Header(None)):
    # Token verification logic
    if token != "3242423":
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return {
        "user": "authorised_user"
    }


@app.get("/secure-data")
def get_secure_data(user=Depends(verify_token)):
    return {
        "message": "This is secure data",
        "user": user
    }


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





from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI KT",
    description="This is a test FastAPI application.",
    version="1.0.0"
)

task_list = []

class Task(BaseModel):
    id: int
    name: str
    completed: bool = False


@app.post("/tasks")
def create_task(task: Task):
    task_list.append(task)
    return {
        "message": "Task added successfully",
        "task": task
    }
@app.get("/tasks")
def get_tasks():
    return task_list

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in task_list:
        if task.id == task_id:
            return task
    return {"message": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(task_list):
        if task.id == task_id:
            task_list[index] = updated_task
            return {"message": "Task updated"}
    return {"message": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            return {"message": "Task deleted"}
    return {"message": "Task not found"}
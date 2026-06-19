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
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.todo import TaskList, Task, TaskNotFoundError
from app.schemas import TaskOut, TaskCreate

app = FastAPI()

app.add_middleware(                                      # 新增这一段
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

task_list = TaskList()
task_list.load()

@app.get("/tasks", response_model=list[TaskOut])
def list_tasks():
    return task_list.tasks

@app.post("/tasks", response_model=TaskOut)
def create_task(payload: TaskCreate):
    task = Task(task_id=task_list.next_id(), title=payload.title)
    task_list.add(task)
    task_list.save()
    return task

@app.put("/tasks/{task_id}/done", response_model=TaskOut)
def mark_done(task_id: int):
    try:
        task = task_list.find_by_id(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="任务不存在")
    task.mark_done()
    task_list.save()
    return task

@app.delete("/tasks/{task_id}")
def delete(task_id:int):
    try:
        task_list.delete(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="任务不存在") 
    task_list.save()
    return {"detail": "已删除"}

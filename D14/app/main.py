from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.todo import TaskList, Task, TaskNotFoundError
from app.schemas import TaskOut, TaskCreate

app = FastAPI()

#中间件：请求 → CORSMiddleware → 你的路由 → CORSMiddleware → 响应
app.add_middleware(                                      
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

task_list = TaskList()
task_list.load()

#读取：不改变任何东西
@app.get("/tasks", response_model=list[TaskOut])
def list_tasks():
    return task_list.tasks

#post新建
@app.post("/tasks", response_model=TaskOut)
def create_task(payload: TaskCreate):
    task = Task(task_id=task_list.next_id(), title=payload.title)
    task_list.add(task)
    task_list.save()
    return task

#put改变状态
@app.put("/tasks/{task_id}/done", response_model=TaskOut)
def mark_done(task_id: int):
    try:
        task = task_list.find_by_id(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="任务不存在")
    task.mark_done()
    task_list.save()
    return task

#delete删除id
@app.delete("/tasks/{task_id}")
def delete(task_id:int):
    try:
        task_list.delete(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="任务不存在") 
    task_list.save()
    return {"detail": "已删除"}

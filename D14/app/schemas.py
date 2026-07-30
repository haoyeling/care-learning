from pydantic import BaseModel
#pydantic数据校验，把外面的脏数据变成干净对象
from datetime import datetime
class TaskCreate(BaseModel):
    title: str

class TaskOut(BaseModel):
    task_id: int
    title: str
    done: bool
    created_at: datetime
    


from pydantic import BaseModel
from datetime import datetime
class TaskCreate(BaseModel):
    title: str

class TaskOut(BaseModel):
    task_id: int
    title: str
    done: bool
    created_at: datetime
    


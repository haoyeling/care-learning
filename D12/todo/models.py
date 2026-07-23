import logging
from datetime import datetime
from .errors import EmptyTitleError
logger = logging.getLogger(__name__)
class Task:
    def __init__(self, task_id, title, done=False, created_at=None):
        if not title.strip():
            raise EmptyTitleError()
        self.task_id = task_id
        self.title = title
        self.done = done
        self.created_at = created_at if  created_at else datetime.now()

    
    def mark_done(self):
        self.done = True
    
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "done": self.done,
            "created_at": self.created_at.isoformat()
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task_id"],
            data["title"],
            data["done"],
            datetime.fromisoformat(data["created_at"]),
            )


    def __str__(self):
        x = "有" if self.done else "没有"
        return f"{self.task_id} {x} {self.title}"
    def __repr__(self):
        return f"Task(task_id={self.task_id!r}, title={self.title!r}, done={self.done!r})" 


    


import logging
from datetime import datetime
from .errors import EmptyTitleError
logger = logging.getLogger(__name__)
class Task:
    def __init__(self, task_id, title, done=False):
        self.task_id = task_id
        self.title = title
        self.done = done
        self.created_at = datetime.now()
        if not self.title.strip():
            raise EmptyTitleError()
    
    def mark_done(self):
        self.done = True
    
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "done": self.done,
            "datetime": self.created_at
        }
    
    def __str__(self):
        x = "有" if self.done else "没有"
        return f"{self.task_id} {x} {self.title}"
    def __repr__(self):
        return f"Task(task_id={self.task_id!r}, title={self.title!r}, done={self.done!r})" 
    


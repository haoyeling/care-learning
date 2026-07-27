import json
from .models import Task
from .errors import TaskNotFoundError
from decorators import timer

class TaskList:
    def __init__(self, filepath="tasks.json"):
        self.tasks = []
        self.filepath = filepath

    def add(self, task):
        self.tasks.append(task)

    def next_id(self):
        if  not self.tasks:
            return 1
        return max([t.task_id for t in self.tasks]) + 1
    
    @timer
    def save(self):
        data = [t.to_dict() for t in self.tasks]
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    def load(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.tasks= [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            self.tasks = [] 

    def find_by_id(self, task_id):
        for t in self.tasks:
                if t.task_id == task_id:
                    return t
        raise TaskNotFoundError(f"找不到任务 id={task_id}")

    def delete(self, task_id):
        task = self.find_by_id(task_id)     # 不存在就直接抛出去了
        self.tasks.remove(task) 
        
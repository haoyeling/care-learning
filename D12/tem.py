import json
from todo import Task

t = Task(1, "买菜")
t2 = Task.from_dict(t.to_dict())
print(t2.created_at, type(t2.created_at))
print(t.created_at == t2.created_at)      # 关键:必须 True
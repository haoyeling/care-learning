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
    
    def to_dict(self):#已有对象，dict，描述它 时间戳
        return {
            "task_id": self.task_id,
            "title": self.title,
            "done": self.done,
            "created_at": self.created_at.timestamp(),   # 给机器
            "created_at_display": self.created_at.strftime("%Y-%m-%d %H:%M"), # 给人
            #时间戳：比较、排序、算时间差、跨语言、跨时区(数据库存储、API传输、日志分析)
            #isoformat:配置文件，给人看导出
        }
    @classmethod#磁盘上文本——>dict——>对象
    def from_dict(cls, data):
        return cls(
            data["task_id"],
            data["title"],
            data["done"],
            datetime.fromtimestamp(data["created_at"]),
            )


    def __str__(self):
        mark = "✓" if self.done else " "
        when = self.created_at.strftime("%m-%d %H:%M")
        return f"[{self.task_id}] {mark} {self.title}  ({when})"
    def __repr__(self):
        return f"Task(task_id={self.task_id!r}, title={self.title!r}, done={self.done!r})" 


    


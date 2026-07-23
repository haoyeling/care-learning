class EmptyTitleError(ValueError):
    """任务标题为空"""


class TaskNotFoundError(Exception):
    """指定 id 的任务不存在"""
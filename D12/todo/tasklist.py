class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def next_id(self):
        if  not self.tasks:
            return 1
        
        return max([t.task_id for t in self.tasks]) + 1

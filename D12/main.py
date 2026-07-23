import argparse
from todo import Task,TaskList, TaskNotFoundError
parser = argparse.ArgumentParser(description="TODO List")
subparsers = parser.add_subparsers(dest="command", required=True)

p_add = subparsers.add_parser("add", help="添加任务")
p_add.add_argument("title", help="任务标题")

p_list = subparsers.add_parser("list", help="列出所有任务")

p_done = subparsers.add_parser("done", help="标记完成")
p_done.add_argument("task_id", type=int, help="任务 id")

p_delete = subparsers.add_parser("delete", help="删除成功")
p_delete.add_argument("task_id", type=int, help="任务 id")

args = parser.parse_args()

tasks = TaskList()
tasks.load()
if args.command == "add":
    task = Task(tasks.next_id(), args.title)
    tasks.add(task)
    tasks.save()
    print("已添加:", task)

elif args.command == "list":
    if not tasks.tasks:
        print("暂无任务")
    for t in tasks.tasks:
        print(t)

elif args.command == "done":
    try:
        task = tasks.find_by_id(args.task_id)
        task.mark_done()
        tasks.save()
        print("已完成:", task)
    except TaskNotFoundError as e:
        print(e)

elif args.command == "delete":
    try:
        tasks.delete(args.task_id)
        tasks.save()
        print(f"已删除任务 {args.task_id}")
    except TaskNotFoundError as e:
        print(e)

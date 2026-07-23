import argparse
from todo import Task,TaskList
parser = argparse.ArgumentParser(description="TODO List")
subparsers = parser.add_subparsers(dest="command", required=True)

p_add = subparsers.add_parser("add", help="添加任务")
p_add.add_argument("title", help="任务标题")

p_list = subparsers.add_parser("list", help="列出所有任务")

p_done = subparsers.add_parser("done", help="标记完成")
p_done.add_argument("task_id", type=int, help="任务 id")

args = parser.parse_args()

tasks = TaskList()

if args.command == "add":
    task = Task(tasks.next_id(), args.title)
    tasks.add(task)
    print("已添加:", task)
elif args.command == "list":
    for t in tasks.tasks:
        print(t)
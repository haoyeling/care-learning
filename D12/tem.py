# import json
# from todo import Task

# t = Task(1, "买菜")
# t2 = Task.from_dict(t.to_dict())
# print(t2.created_at, type(t2.created_at))
# print(t.created_at == t2.created_at)      # 关键:必须 True
def logged(fn):
    print(">>> logged 被调用了")
    def wrapper():
        print("--- 开始 ---")
        fn()
        print("--- 结束 ---")
    print(">>> wrapper 造好了，但还没跑")
    return wrapper

def save():
    print("正在保存")

print("=== 装饰前 ===")
save = logged(save)
print("=== 装饰后，还没调用 ===")
save()
print("=== 调用完了 ===")

def show(*args, **kwargs):
    print("位置:", args)
    print("关键字:", kwargs)

show(1, "a", x=10, y=20)
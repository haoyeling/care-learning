# 两个班的学生名单
class_a = {"张三", "李四", "王五", "赵六"}
class_b = {"李四", "王五", "钱七"}

class_both = class_a & class_b
class_all = class_a | class_b
class_a_only = class_a - class_b
class_only_ab = class_a ^ class_b

print(class_both)
print(class_all)
print(class_a_only)
print(class_only_ab)
if "张三" in class_a:
    print("张三在班级a中")
nums = [1,2,2,3,3,3]
unique_nums = set(nums)
num = len(unique_nums)
print(f"一共有{num}个不同的数，分别是{unique_nums}")

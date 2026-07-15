# 1. 一组学生记录,每条是 (姓名, 年龄, 城市)
students = [
    ("张三", 20, "北京"),
    ("李四", 22, "上海"),
    ("王五", 21, "天津"),
]
total = 0
count = 0
for student in students:
    name, age, city = student
    print(f"{name}, {age}岁, 来自{city}")
    total = total + age
    count += 1
average_age = total / count
print(f"平均年龄是： {average_age: .1f}")
# students[0][1] = 99 元组不支持修改

def get_min_max(nums):
    return min(nums), max(nums)
low, high = get_min_max([3, 1, 4, 1, 5])
print(low)
print(high)
#元组：可以解包，一个元素分三个值
age = int(input("请输入年龄："))
ticket_input = input("有票吗？(y/n):")
has_ticket = (ticket_input == 'y')      # 布尔值,只有 True 和 False 两个值(注意首字母大写!)
if age >= 18 and has_ticket:
    print("可以入场")
elif age < 18:
    print("未成年不可入场")
else:
    print("请先买票")

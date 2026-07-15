import json
with open('output.txt', 'w') as f:
    f.write("第一行\n")
    f.write("第二行\n")

print("写入完成")

data = {"张三": {"phone": "175"}}

#写：字典 ——> 文件
with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

#读： 文件 ——> 字典
with open('data.json') as f:
    data = json.load(f)

#第一次运行,文件还不存在,就用空字典
try:
    with open('contacts.json') as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}
import json

FILENAME = "contacts.json"

def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        return True
    else:
        return False

def search_contact(contacts, name):
    if name in contacts:
        return contacts.get(name) # 找到返回字典,找不到自动返回 None
    else:
        return None
    
def list_contacts(contacts):
    if not contacts:
        print("通讯录是空的")
        return
    for name, info in contacts.items():
        print(f"{name}: 手机号：{info['phone']} / 电子邮件：{info['email']}")

def save_contacts(contacts):
    with open(FILENAME, 'w') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def load_contacts():
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

contacts = load_contacts()

while True:
    print("1.添加  2.删除  3.查找  4.列出全部  5.退出")
    choice = input("请选择：")
    if choice == "1":
        name = input("姓名：")
        phone = input("手机: ")
        email = input("邮件: ")
        add_contact(contacts, name, phone, email)
        save_contacts(contacts)
    elif choice == "2":
        name = input("想要删除的人是： ")
        if delete_contact(contacts, name):
            save_contacts(contacts)
            print("已删除")
        else:
            print("删除失败")
    elif choice == "3":
        name = input("请输入查找姓名： ")
        result = search_contact(contacts, name)
        if result:
            print(f"{name}: {result['phone']} / {result['email']}")
        else:
            print("没找到这个人")
    elif choice == "4":
        list_contacts(contacts)
    elif choice == "5":
        save_contacts(contacts)
        break

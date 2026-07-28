class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def validate_phone(self):
        if len(self.phone) != 11:
            return False
        for num in self.phone:
            if not num.isdigit():
                return False
        return True
    def to_dict(self):
     return {
         "name": self.name,
         "phone": self.phone,
         "email": self.email,
     }
    # 另一种写法,直接写入字典
 
    def __str__(self): #print（a）/str(a)/f“{a}” 面向终端用户，好读
        return f"{self.name} | {self.phone} | {self.email}"
    def __repr__(self): #print([a]) / 任何容器里的元素，面向开发者，准确无歧义
        return f"{type(self).__name__}(name={self.name!r}, phone={self.phone!r}, email={self.email!r})" #字符串取!r会自带引号

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)
    
    def count(self):
        return len(self.contacts)
    
    def find_by_name(self, name):
        for c in self.contacts:
            if c.name == name:
                return c
        return None

class Colleague(Contact):
    def __init__(self, name, phone, email, company, title):
        super().__init__(name, phone, email) # 先让父类干它那部分
        self.company = company
        self.title = title
        type(self).__name__
    # def __str__(self):
        # return f"{self.name} | {self.phone} | {self.email} | {self.company}  {self.title}"
    def __str__(self):
        return f"{super().__str__()} | {self.company} {self.title}"


class Family(Contact):
    def __init__(self, name, phone, email, relation):
        super().__init__(name, phone, email)
        self.relation = relation
    def __str__(self):
        return f"{super().__str__()} | {self.relation}"



book = AddressBook()
book.add(Contact("张三", "13800000000", "z@b.com"))
book.add(Contact("李四", "13900000000", "l@b.com"))
print(book.count())                    # 期望 2
print(book.find_by_name("张三").phone)  # 期望 13800000000
print(book.find_by_name("王五"))        # 期望 None
print(book.find_by_name("李四"))   # 期望：一个 Contact 对象，不是 None


book.add(Colleague("王五", "13700000000", "w@b.com", "字节跳动", "技术专家"))
book.add(Family("妈妈", "13600000000", "m@b.com", "母亲"))
print(book.count())                       # 期望 4
print(book.find_by_name("王五"))           # 期望带公司职位的那行
print(book.find_by_name("王五").validate_phone())   # 期望 True
print(book.contacts)


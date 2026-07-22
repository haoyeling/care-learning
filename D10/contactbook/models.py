from .errors import InvalidPhoneError
print("我是", __name__)
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        if not self.validate_phone():
            raise InvalidPhoneError(f"手机号不合法: {phone}")
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
 
    def __str__(self): #print（a）/str(a)/f“{a}”
        return f"{self.name} | {self.phone} | {self.email}"
    def __repr__(self): #print([a]) / 任何容器里的元素
        return f"{type(self).__name__}(name={self.name!r}, phone={self.phone!r}, email={self.email!r})" #字符串取!r会自带引号


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

if __name__ == "__main__":
    print("models.py 被执行了")
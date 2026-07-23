class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def validate_phone(self):
        if len(self.phone) != 13:
            return False
        for num in self.phone:
            if not num.isdigit():
                return False
        return True
    
#def的另一种写法
    #
    #def validate_phone(self):
    #    return  len(self.phone) == 11 and self.phone.isdigit()
    # isdigit() 不只字符串的单个字符能用，整个字符串也能用——它检查的就是"是否所有字符都是数字"
    # and 有短路特性：左边是 False 就直接出结果，右边根本不执行。

    def to_dict(self):
        count = {}
        count ['name'] = self.name
        count ['phone'] = self.phone
        count ['email'] = self.email
        return(count)  
    
    # def to_dict(self):
    # return {
        # "name": self.name,
        # "phone": self.phone,
        # "email": self.email,
    # }
    # 另一种写法,直接写入字典

a = Contact("A", "17526558848", "a@b.com")
print(a.validate_phone())
print(a.to_dict())
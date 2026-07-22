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
        count = {}
        count ['name'] = self.name
        count ['phone'] = self.phone
        count ['email'] = self.email
        return(count)  

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

book = AddressBook()
book.add(Contact("张三", "13800000000", "z@b.com"))
book.add(Contact("李四", "13900000000", "l@b.com"))
print(book.count())                    # 期望 2
print(book.find_by_name("张三").phone)  # 期望 13800000000
print(book.find_by_name("王五"))        # 期望 None
print(book.find_by_name("李四"))   # 期望：一个 Contact 对象，不是 None
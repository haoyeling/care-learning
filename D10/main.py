print("我是", __name__)
from contactbook import Contact, Colleague, Family, AddressBook

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


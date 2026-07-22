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
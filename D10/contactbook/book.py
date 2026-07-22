import logging
logger = logging.getLogger(__name__)
class AddressBook:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)
        logger.info("已添加联系人: %s", contact.name)
    
    def count(self):
        return len(self.contacts)
    
    def find_by_name(self, name):
        for c in self.contacts:
            if c.name == name:
                return c
        return None
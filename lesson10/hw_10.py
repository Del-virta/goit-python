
from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data = record
    
class Record:
    def __init__(self, name):
        self.name = name
        self.phone = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.remove(phone)

    def add_phone(self, phone):
        pass

class Field:
    pass

class Name(Field):
    record_name = 'name'
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

name = Name('Bob')
phone = Phone('12335478896')
phone_1 = Phone('122458745445')
record_1 = Record(name)
record_1.add_phone(phone)
record_1.add_phone(phone_1)
address_book = AddressBook()
address_book.add_record(record_1)
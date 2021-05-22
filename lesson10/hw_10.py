
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

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, phone_1, phone_2):
        self.remove_phone(phone_1)
        self.add_phone(phone_2)


class Field:
    pass

class Name(Field):
    record_name = 'name'
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone


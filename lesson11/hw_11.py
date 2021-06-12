
from collections import UserDict
import datetime
import re

class AddressBook(UserDict):

    def add_record(self, name, record):
        self.data[name] = record
    def iterator(self, n=0):
        records = list(self.data.items())
        if len(records)<=n:
            result = '\n'.join([f'{record[0]}: {record[1]}' for record in records])
            return result
        else:
            while records:
                result = '\n'.join([f'{record[0]}: {record[1]}' for record in records[;n]])
                yield result
                records = records[n:]

        

    
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
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

class Name(Field):
    record_name = 'name'
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_phone):
        valid_phone = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{3}[-\.\s]??\d{2}[-\.\s]??\d{2}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{2}[-\.\s]??\d{2})'
        if not re.search(valid_phone, str(new_phone)):
            raise ValueError(f'{new_phone} is invalid. Please enter a 10 or 12 digit phone number.')
        else:
            self.__value = new_phone

class Birthday(Field):
    def __init__(self, birth_date):
        self.__birth_date = birth_date

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        try:
            valid_birth_date = datetime.strptime(birth_date, '%d.%m.%Y')
            self.__birth_date = valid_birth_date
        except ValueError: 
            return 'Input data is invalid'

        

    def days_to_birthday(self, birth_date):    
        current_date = datetime.now()
        birthday = birth_date.replace(year = current_date.year)
        if current_date>birthday:
            birthday = birthday.replace(year = current_date.year+1)
        delta = birthday-current_date
        return f'{delta} days left to birthday!'
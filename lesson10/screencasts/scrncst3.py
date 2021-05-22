from collections import UserDict, UserList

class User(UserDict):
    def get_name(self):
        return self.data["name"]

    def add_phone(self, phone):
        '''if phone not in self.data:
            phones = []
        else:
            phone = self.data["phones"]'''
        phones = self.data.get('phones', [])
        phones.append(phone)
        self.data["phones"] = phones

    def get_phones(self):
        return self.data['phones']


user = User()
user['name'] = 'Bob'
user.add_phone('11 222 333')
user.add_phone('11 222 777')
print(user)
print(user.get_phones())
print(user.get_name())

class Phones(UserList):
    def add(self, val):
        self.data.append('+38' + val)

    def get_operator_codes(self):
        codes = []
        for phone in self.data:
            codes.append(phone[3:6])
        return codes

phones = Phones()
phones.add('0501236587')
phones.add('0991236587')

print(phones.get_operator_codes())




class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({
            'id':self.current_id, 
            'name':name, 
            'phone':phone, 
            'email':email, 
            'favorite':favorite})
        self.current_id+=1
        
        

a = Contacts()
a.add_contacts('Wylie Pope', '(692) 802-2949', 'est@utquamvel.net', True)
a.add_contacts('Bob', '(6233) 567-2949', 'est@utmvel.net', False)
print(a.list_contacts())
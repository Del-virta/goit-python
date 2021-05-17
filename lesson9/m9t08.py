def get_emails(list_contacts):
    return list(map(lambda x: x['email'], list_contacts))
    

contact_list = [
    {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
    {"name": "Allen Raymond2", "email": "nulla.ante2@vestibul.co.uk", "phone": "(292) 914-3792", "favorite": False},
    {"name": "Allen Raymond3", "email": "nulla.ante3@vestibul.co.uk", "phone": "(392) 914-3792", "favorite": False}
]

print(get_emails(contact_list))


    

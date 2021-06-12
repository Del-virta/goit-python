from lesson12.hw_12 import AddressBook, Record, Name, Phone, Birthday
import re
import pickle
from  pathlib import Path

# File for saving data
file = 'contacts.txt'
# group exit commands in list
exit_commands = ['good bye', 'close', 'exit']


def say_hello():
    return 'How can I help you?'
# Making class objects dor arguments
def add_contact(name, phone, birthday=None):    
    c_name = Name(name)
    c_phone = Phone(phone)
    c_birthday = Birthday(birthday)
    c_record = Record(name=c_name, phone=c_phone, birthday=c_birthday)
    if name in contacts:
        # Using Record class method to add phone to list if name is in a contacts
        contacts.add_phone(c_phone)
    else:
        # Using AddressBook class method to add a record to dictionary if name is unique
        contacts.add_record(c_record)
        return f'Contact {name} is in your phone book now!'


def change_contact(name, phone, new_phone):
    if name in contacts:
        # Using Record method to change phone number
        contacts[name].change_phone(phone, new_phone)
        return f'Contact {name} number is changed now!'        
    else:
        raise ValueError

def find_contact(name):
    # Searching contact phones using name
    if name in contacts:
        return f'{name} number is {contacts[name]}'
    else:
        raise ValueError

def iter_print():
    # AddressBook method for printing just a part of data
    contacts.iterator(10)

def print_contacts():
    # Printing the whole contact dict
    contact_list = []
    for name, number in contacts.items():
        contact_list.append(f'{name} | {number}')
    return '\n'.join(contact_list)

def look_up(user_input):
    # Searching for matching pattern in names and fhones using class AddressBook method
    pattern = re.split(' ',user_input)
    result = contacts.full_search(pattern)
    return result

# Error processing decorator
def input_error(command):
    def inner(*args):
        try:            
            return command(*args)        
        except KeyError:
            return 'There is no such a command'
        except ValueError: 
            return 'Input data is invalid'
        except IndexError:
            return 'This contact already exists'
    return inner

commands = {
        'hello': say_hello,
        'add': add_contact,
        'change': change_contact,
        'phone': find_contact,
        'find': look_up,
        'show all': print_contacts,
        'print': iter_print
    }

@input_error
# Commands parser
def parse_command(user_input):
    for command in commands:
        if user_input.startswith(command):
            return commands[command]    
    raise KeyError('No such command!')
    
# Names parser
def parse_name(user_input):
    user_input_list = re.split(' ', user_input)
    if len(user_input_list)>1:
        name = user_input_list[1]
    return name
# Birthday parser
def parse_birthday(user_input):
    if len(re.split(' ', user_input))==3:
        birthday = re.split(' ', user_input)[3]
    return birthday

@input_error
# Phone number parser
def parse_number(user_input):
    user_input_list = re.split(' ', user_input)
    if len(user_input_list)==3:
        if user_input_list[2].isdigit and len(user_input_list[2]) == 12:
            number = '+' + user_input_list[2]
        elif user_input_list[2].isdigit and len(user_input_list[2]) == 10:
            number = '+38' + user_input_list[2]
        else:
            raise ValueError
    return number

@input_error
# Command handler
def handle_command(command,user_input):
    if command == 'add':
        name = parse_name(user_input)
        phone = parse_number(user_input)
        birthday = parse_birthday(user_input)
        result = commands[command](name, phone, birthday) 
        return result
    elif command =='change':
        name = parse_name(user_input)
        phone = parse_number(user_input)
        new_phone = parse_birthday(user_input)
        result = commands[command](name, phone, new_phone) 
        return result
    elif command == 'phone':
        name = parse_name(user_input) 
        return commands[command](name)
    elif command == 'find':
        return commands[command](user_input)
    else:
        return commands[command]()        


def main():
    # Some useful tips
    print('Hi! This is a little bot, it will help you with the contact book. Bot knows some useful commands:')
    print('hello - just to be polite,')
    print('add - to add a new contact,')
    print('change - to change an existing number,')
    print('phone - to look up the number using name,')
    print('show all - to see the whole contact book,')
    print('print - to see first 5 records in contact book,')
    print('find - to search for matching patterns in names or phones in contact book')
    print('If you need bot no more, you can just type good bye, close or exit. Have fun!')
    
    while True:
        user_input = input('').lower()
        if user_input in exit_commands:
            print('Good bye!')
            # Saving data to file
            with open(file, 'wb') as fh:
                pickle.dump(contacts, fh)
            break
        else:
            print(handle_command(user_input))

if __name__ == '__main__':
    contacts = AddressBook()
    # Loading data from file
    if Path(file).exists:
        with open(file, rb) as fh:
            contacts = pickle.load(fh)
    main()
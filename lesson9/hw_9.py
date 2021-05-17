import re

exit_commands = ['good bye', 'close', 'exit']
phone_book = {}

def say_hello():
    print('How can I help you?')

def add_contact(name, number):
    if name in phone_book:
        raise IndexError
    else:
        phone_book[name] = number

def change_contact(name, number):
    if name in phone_book:
        phone_book[name] = number
    else:
        raise KeyError

def find_contact(name):
    if name in phone_book:
        print(phone_book[name])
    else:
        raise KeyError

def print_contacts():
    for name, number in phone_book.items():
        print(f'{name}: {number}')

def input_error(command):
    def inner(*args):
        try:
            a = command(*args)
            return a        
        except KeyError:
            print('There is no such a contact')
        except ValueError: 
            print('Please enter your command')
        except IndexError:
            print('This contact already exists')
    return inner

commands = {
        'hello': say_hello,
        'add': add_contact,
        'change': add_contact,
        'phone': find_contact,
        'show all': print_contacts,
    }

def parse_command(user_input):
    user_input_list = re.split(' ', user_input)
    if len(user_input_list)>0:        
        if user_input_list[0] in commands:
            command = user_input_list[0]
        else:
            raise ValueError
    return command

def parse_name(user_input):
    user_input_list = re.split(' ', user_input)
    if len(user_input_list)>1:
        name = user_input_list[1]
    return name


def parse_number(user_input):
    user_input_list = re.split(' ', user_input)
    if len(user_input_list)==3:
        if user_input_list[2].isdigit and len(user_input_list[2]) == 12:
            number = '+' + user_input_list[2]
        elif user_input_list[2].isdigit and len(user_input_list[2]) == 10:
            number = '+38' + user_input_list[2]
        else:
            print('Entered number is invalid')
    return number

@input_error
def handle_command(command, user_input):
    if command in ['add','change']:
        name = parse_name(user_input)
        number = parse_number(user_input)
        return commands[command](name, number)
    elif command == 'phone':
        name = parse_name(user_input)
        return commands[command](name)
    else: 
        return commands[command]


def main():
    print('Hi! This is a little bot, it will help you with the contact book. Bot knows some useful commands:')
    print('hello - just to be polite,')
    print('add - to add a new contact,')
    print('change - to change an existing number,')
    print('phone - to look up the number using name,')
    print('show all - to see the whole contact book.')
    print('If you need bot no more, you can just type good bye, close or exit. Have fun!')
    
    while True:
        user_input = input('').lower()
        if user_input in exit_commands:
            print('Good bye!')
            break
        else:
            command = parse_command(user_input)
            handle_command(command, user_input)

if __name__ == '__main__':
    main()
from random import randint

def get_random_password():
    i = 0
    password = ""
    while i < 8:
        password+=chr(randint(40,126))
        i+=1
    return password
print(get_random_password())
import string
def is_valid_password(password):
    is_upper = None
    is_lower = None
    is_number = None
    is_eight_len = None
    if len(password) == 8:
        is_eight_len = True
    for char in password:
        if char in string.ascii_lowercase:
            is_lower = True
        elif char in string.ascii_uppercase:
            is_upper = True
        try:
            if type(int(char)) == int:
                is_number = True
        except ValueError:
            pass
    if is_number and is_lower and is_eight_len and is_upper:
        return True
    else:
        return False
print(is_valid_password('3WTc1oFv')) 
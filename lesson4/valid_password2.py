def is_valid_password(password):
    if len(password) != 8:
        return False
    else:
        result = 0
        for symbol in password:
            if ord(symbol) in (65, 90):
                result += 1
            elif ord(symbol) in (97, 122):
                result += 1
            elif  ord(symbol) in (48, 57):
                result += 1
            else:
                result = 0
        if result >= 3:
            return True
        else:
            return False

print(is_valid_password('3WTc1oFv')) 
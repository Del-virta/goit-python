def is_valid_pin_codes(pin_codes):
    is_four=True
    is_number = True
    is_string = True
    not_same = True
    if len(pin_codes)<1:
        return False
    for pin in pin_codes:
        if len(pin)!=4:
            is_four = False
        if type(str(pin)) != str:
            is_string = False
        try:
            for number in pin:
                if type(int(number)) == int:
                    is_number = True
        except ValueError:
            return False
        if len(set(pin_codes))<len(pin_codes):
            not_same = False
    if is_four and is_string and is_number and not_same:
        return True
    else:
        return False
print(is_valid_pin_codes(['1101', '9034', '00112']))
            
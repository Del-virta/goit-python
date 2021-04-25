import string
def is_equal(utf_8_pass, utf_16_pass):
    pass1 = utf_16_pass.decode('utf-16')
    pass2 = utf_8_pass.decode('utf-8')
    if pass1.casefold() == pass2.casefold():
        is_equal = True
    else:
        is_equal = False
    return is_equal
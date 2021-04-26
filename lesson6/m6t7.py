def is_equal(utf_8_pass, utf_16_pass):
    if utf_8_pass.decode('utf-8') == utf_16_pass.decode('utf-16'):
        is_equal = True
    else:
        is_equal = False
    return is_equal
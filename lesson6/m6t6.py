def encode_password(password):
    symbol_list = []
    byte_pass = password.encode()
    for symbol in byte_pass:
        symbol_list.append(hex(symbol))
    return symbol_list
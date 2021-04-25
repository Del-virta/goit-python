def write_to_bin(path, user_info):
    some_list = []
    with open(path, 'wb') as fh:
        for key, value in user_info.items():
            fh.write(f'{key}:{value}\n')
        fh.close()

    with open(path, 'rb') as fh:
        for position in fh.readlines():
            without_n = position.decode('utf-8')
            without_n = without_n.split('\n')
            some_list.append(without_n[0])
    return some_list
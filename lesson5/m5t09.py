def formatted_numbers():
    num_list = []
    num_list.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
    for i in range(16):
        num_list.append('|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i))
    return num_list

for el in formatted_numbers():
    print(el)
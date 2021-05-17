def normal_name(list_name):
    new_list = []
    for i in map(lambda x: x.capitalize(), list_name):
        new_list.append(i)
    return new_list
print(normal_name(["dan", "jane", "steve", "mike"]))
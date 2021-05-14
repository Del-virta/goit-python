def flatten(data):    
    if len(data)<1:
        return []
    elif type(data[0]) == list:
        return flatten(data[0]) + flatten(data[1:])
    elif type(data[0]) != list:
        return [data[0]] + flatten(data[1:])

print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
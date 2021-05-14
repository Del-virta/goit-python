def encode(data):
    if len(data)<1:
        return []
    else:
        i = 1
        while i < len(data) and data[i] == data[0]:
            i += 1
        return list(data[0:1]) + [i] + encode(data[i:])

print(encode(['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']))
print(encode("XXXZZXXYYYZZ"))
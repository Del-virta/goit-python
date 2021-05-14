'''def my_decode(data):
    stroka = ''
    if data == []:
        return []
    else:
        for i in range(len(data)):
            if type(data[i]) != int:
                stroka += data[i]*int(data[i+1])
        return list(stroka)'''

def decode(data):
    if data == []:
        return []
    else:
        chars = data[0]*data[1]
        return list(chars) + decode(data[2:])

print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))
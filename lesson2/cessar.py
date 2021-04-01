import string
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
alpha = string.ascii_lowercase
ALPHA = string.ascii_uppercase
n = len(alpha)
encoded_message = ""
for ch in message:
    if ch in alpha:
        encoded_message = encoded_message + alpha[(alpha.find(ch) + offset) % n]
    elif ch in ALPHA:
        encoded_message = encoded_message + ALPHA[(ALPHA.find(ch) + offset) % n]
    else:
        encoded_message = encoded_message + ch
print(encoded_message)  

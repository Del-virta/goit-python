sum = 0
while True:
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
    i = 0
    while i <= num:
        sum+=i
        i+=2
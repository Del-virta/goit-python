num = int(input("Введите целое число (0 для выхода): "))
sum = 0
while num !=0:
    i = 0
    while i <= num:
        sum+=i    
        i+=1
    num = int(input("Введите целое число (0 для выхода): "))
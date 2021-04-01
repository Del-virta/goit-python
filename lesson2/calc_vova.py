result = 0.0
operand = 0.0
operator = None
wait_for_number = True
zero_division_test = 3

while True: #Запрашиваем_операнд
    try:
        operand = float(input("Введите число: "))
        result = operand
        operand = 0.0
        break
    except ValueError:
        print("Вы ввели не число!")
        continue

while True:
    while True: #Запрашиваем_оператор
        operator = input("Введите знак: ")
        if operator not in ('+', '-', '*', '/', '='):
            print("Вы ввели не знак +,-,*,/ или =")
        else:
            break

    while True: #Запрашиваем_операнд
        if operator in ('='): #удостоверимся, что нам не нужно повторно его запрашивать
            break
        try:
            operand = float(input("Введите число: "))
            if operator in ('/'): #проверка деления на ноль
                zero_division_test /= operand
            break
        except ValueError:
            print("Вы ввели не число!")
            continue
        except ZeroDivisionError:
            print("На ноль мы не делим. Введите другое число")

    if operator == '+': #Решаем
        result = result + operand
    elif operator == '-':
        result = result - operand
    elif operator == '*':
        result = result * operand
    elif operator == '/':
        result = result / operand
    elif operator == '=':
        break
print(f"Ваш результат: {result}")
while True:
    result = input('Please type any number: ')
    try:
        result = float(result)
    except ValueError or TypeError:
        print(f'{result} is not a number')
    else:
        break
while True:
    operator = input("Please type any operation: ")
    if operator == "=":
        break
        result = result  
    elif operator not in ["+","-","*","/"]:
        print(f"Input {operator} is not an operation")
        continue      
    operand = input("Please type any number: ")
    if operand == "=":
        break
        result = result  
    try:
        operand = float(operand)
    except ValueError:
        print(f"Input {operand} is not a number")
        operand = input("Please type any number: ")
        while True:
            try:
                operand = float(operand)
            except ValueError:
                print(f"Input {operand} is not a number")
                operand = input("Please type any number: ")
                operand = float(operand)
                break
    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    elif operator == "/":
        result /= operand        
print(result)
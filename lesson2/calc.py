result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number == True:      
        operand = input(" ")
        if operand == "=":            
            print(result)
            break
        try:
            operand = float(operand)
            wait_for_number = False
            if operator == None:                
                result = operand
            elif operator == "+":
                result = result + operand
            elif operator == "-":
                result = result - operand
            elif operator == "*":
                result = result * operand
            elif operator == "/":
                try:
                    result = result / operand
                except ZeroDivisionError:
                    print("Деление на ноль")
        except ValueError:
            print(f"{operand} is not a number. Try again!")
            
    elif wait_for_number == False:
        operator = input(" ")
        if operator == "=":
            print(result)
            break
        elif not operator in ("+","-","/","*"):            
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again!")
        else:
            wait_for_number = True                            
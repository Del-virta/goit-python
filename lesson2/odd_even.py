number = 0

while True:
    if number % 2:
        print(f"{number} is odd")
    else:
        print(f"{number} is even")

    if number > 20:
        break
    number = number + 1

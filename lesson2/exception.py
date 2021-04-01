while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >=18:
            print("You are adult.")
        break
    except ValueError:
        print(f"{age} is not a number")
    finally:
        print("================\n")
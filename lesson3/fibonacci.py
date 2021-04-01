def main():
    n = int(input("Введите положительное целое число: "))
    return n

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    n = main()
    print(f"{n}-й член ряда фибоначчи равен: {fibonacci(n)}")
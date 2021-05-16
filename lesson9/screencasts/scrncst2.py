def outer():
    cache = {}
    def inner_func(y):
        print(cache)
        if y not in cache:
            acumulator = 0
            for i in range(1, y+1):
                acumulator+=i
            cache[y] = acumulator
            print(cache[y])
    return inner_func

def main():
    inner = outer()
    print(inner(10))
    print(inner(10))

if __name__ == '__main__':
    main()
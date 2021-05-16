def caching_fibonacci():
    cache = {0:0,1:1}

    def fibonacchi(n):
        if n in cache:
            return cache[n]
        cache[n] = fibonacchi(n-1)+fibonacchi(n-2)
        return cache[n]

    return fibonacchi

some_cash = caching_fibonacci()
print(some_cash(1000))

def log_decorator(func):
    def first_inner(*args, **kwargs):
        print(f'{func.__name__} called with {args} {kwargs}')
        return func(*args, **kwargs)
    return first_inner

def log_result(func):
    def second_inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} resulted with {result}')
        return result
    return second_inner
    


@log_result
@log_decorator
def sum_(x,y):
    return x + y


def main():
    sum_(2,3)
    #print(sum_(28,7))

if __name__ == '__main__':
    main()

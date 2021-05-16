def hi(name):
    print(f'Hi {name}')

def hello(name):
    print(f'Hello {name}')

FUNCTIONS = {
    'h': hello,
    'r': hi
}

def greeting(mod):
    return FUNCTIONS.get(mod, hi)

def main():
    mod = 'h'
    hi_func = greeting(mod)
    hi_func('Bill')

if __name__ == '__main__':
    main()
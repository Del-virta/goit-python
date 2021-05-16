import collections

d = collections.deque(maxlen=5)

for i in range(10):
    d.append(i)
print(d)

def main():
    user_inputs = collections.deque(maxlen=5)
    while True:
        user_input = input("Input something: ")
        user_inputs.append(user_input)
        if user_input == 'q':
            break
    print(f'last 5 inputs: {user_inputs}')

if __name__ == "__main__":
    main()
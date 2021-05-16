squares = []
for i in range(11):
    squares.append(i ** 2)
print(squares)

# Using comprehensions

squares_new = [i **2 for i in range(11)]
print(squares_new)

# using function and comprehensions

def func(x):
    return x * 2
# with list
dubbled = [func(i) for i in range(11)]
print(dubbled)
# with set
dubbled_set = {func(i) for i in range(11)}
print(dubbled_set)
# with dictionary
dubbled_dict = {i: func(i) for i in range(11)}
print(dubbled_dict)

from functools import reduce


def sum_numbers(numbers):
    return reduce((lambda x,y:x+y), numbers)
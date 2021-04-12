import sys


def parse_args():
    res = ''
    for arg in sys.argv:
        res = res + arg + ' '      
    return res
print(parse_args())
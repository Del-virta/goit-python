import re
import pathlib
def add_order(order, path):
    count = 0
    fh = open(path, 'a')
    fh.write(f'{order}\n')
    fh.close()
    fh = open(path, 'r')
    for orders in fh.readlines():
        if re.search(':active',orders):
            count+=1
    fh.close()
    return count

order = 'Burger:active'
path = pathlib.Path('E:/test.txt')
print(add_order(order,path))

import re
import sys
import pathlib
def read_file(path):
    summa = 0
    fh = open(path, 'r')
    lines = fh.readlines()
    for line in lines:
        number_in_line = re.findall('\d+',line)
        summa+=float(number_in_line[0])
    fh.close()
    return summa
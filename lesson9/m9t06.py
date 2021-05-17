import re

def generator_numbers(string = ""):
    num_list = re.split(r'(\d+)', some_txt)
    for ch in num_list:
            if ch.isdigit():
                yield ch    

def sum_profit(string):
    summa = 0
    for i in generator_numbers(string):
        summa += int(i)
    return summa

some_txt = "The resulting profit was: from the southern possessions $123, from the northern colonies $45, and the king gave $67890"
print(sum_profit(some_txt))



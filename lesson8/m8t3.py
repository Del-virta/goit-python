from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    summa = 0
    getcontext().prec = signs_count
    for i in range(len(number_list)):
        summa+=Decimal(number_list[i])

    return Decimal(summa)/Decimal(len(number_list))
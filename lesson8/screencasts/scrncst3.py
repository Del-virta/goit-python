from decimal import Decimal, getcontext
getcontext().prec = 6
print(Decimal(0.2)+Decimal(0.3))
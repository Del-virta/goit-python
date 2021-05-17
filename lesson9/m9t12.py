from functools import reduce


def amount_payment(payment):    
    return reduce((lambda x,y:x+y), list(filter(lambda x: x>0, payment)))

payment = [1, -3, 4]
print(amount_payment(payment))
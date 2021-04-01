first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))

nod = first if first < second else second
while not (second % nod == 0 and first % nod == 0):
    nod = nod - 1
print(nod)
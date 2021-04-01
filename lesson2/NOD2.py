first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
nod = first + second
while first!= 0 and second !=0:
    if first > second:
        first = first % second
    else:
        second = second % first
nod = first + second
print(nod)
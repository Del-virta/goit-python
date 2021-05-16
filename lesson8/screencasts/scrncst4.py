import math
import cmath

a = 0.55
b = 5
print(math.sin(a))
print(math.asin(a))
print(math.cos(a))
print(math.acos(a))
print(math.tan(a))
print(math.atan(a))

# вычисление расстояния Евклида между точками
print(math.hypot(a)) 

# Преобразование углов и радианов:
print(math.degrees(a))
print(math.radians(a))

# Гиперболические функции:
print(math.sinh(a))
print(math.asinh(a))
print(math.cosh(a))
print(math.acosh(b))
print(math.tanh(a))
print(math.atanh(a))

# Cтепенные функции:
print(math.exp(a))
print(math.pow(b,a)) # преобразует аргументы во float в отличие от встроенной pow
print(math.sqrt(a))
print(math.log2(a))
print(math.log10(a))
print(math.log(a)) # log логарифм с основанием e если основание не задано или с заданным основанием

# Kонстанты:
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf) #infinity
print(math.nan)

# Работа с комплексными числами
print(cmath.sqrt(cmath.pi))

import collections

d = collections.defaultdict(list)
l = ['apple', 'banana', 'apricot', 'peach', 'plum', 'cherry']
for element in l:
    d[element[0]].append(element)
print(d) # defaultdict(<class 'list'>, {'a': ['apple', 'apricot'], 'b': ['banana'], 'p': ['peach', 'plum'], 'c': ['cherry']})

def a():
    return 1

slovar = collections.defaultdict(a)
s = 'i do not know what to write here but it should not be empty'
for i in s:
    slovar[i]+=1
print(slovar)
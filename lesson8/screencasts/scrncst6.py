import collections

s = 'abracadabra56'
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d) # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1, '5': 1, '6': 1}

e = collections.Counter(s)
print(e) # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1, '5': 1, '6': 1})
print(e['a']) #5
print(e.most_common(2)) # [('a',5),('b',2)]

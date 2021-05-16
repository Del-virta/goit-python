import collections

person1 = ('Bob', 'Dou', 25)
Person = collections.namedtuple('Person', ['name', 'surname', 'age'])
person = Person('Jack', 'Watson', 55)
print(person1[0])
print(person.age)
print(person)
print(person1)
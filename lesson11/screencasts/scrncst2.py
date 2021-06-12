class Human:
    def __init__(self,name,age):
        self.__name = None
        self.__age = None
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return f'Human, name: {self.__name}'

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, value):
        self.__name = value

    @age.setter
    def age(self, value):
        value = int(value)
        if value <= 0:
            raise Exception('Age should be > 0')
        self.__age = value

bob = Human('Bob', '20')
print(bob.name, bob.age)

class User:
    name = ''
    age = 0

    def say_hello(self):
        print(f'Hi! I am {self.name}.')

user1 = User()
user1.name = 'Bob'

user2 = User()
user2.name = 'Alice'

user1.say_hello()
user2.say_hello()
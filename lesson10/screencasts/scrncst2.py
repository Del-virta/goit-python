class Person:
    name = ''

    def set_name(self, val):
        self.name = val

    def say_hello(self):
        return f'Hello! I am {self.name}.'


class Manager(Person):
    def give_order(self):
        hello_string = self.say_hello()
        return f'{hello_string} Do your job!'

class Developer(Person):
    def write_code(self):
        return 'Some code here.'
        
class TeamLead(Manager, Developer):
    def give_order(self):
        return f'Write code!'
    

team_lead = TeamLead()
team_lead.set_name('Alice')

print(team_lead.write_code())
print(team_lead.give_order())


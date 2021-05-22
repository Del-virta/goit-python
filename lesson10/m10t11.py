from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for symbol in self.data:
            if symbol.isdigit():
                count+=1                
        return count 

print(NumberString('hjgdfhdshf654gcfj65').number_count())
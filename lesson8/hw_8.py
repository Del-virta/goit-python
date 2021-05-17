from datetime import date, datetime, timedelta
from collections import defaultdict


def congratulate(users):
    day_interval = {0:5,1:4,2:3,3:2,4:1,5:7,6:6}
    start_date = datetime.now() + timedelta(days = day_interval[datetime.now().weekday()])
    end_date = start_date + timedelta(days = 7)

    user_birth = defaultdict(list)
    
    while start_date < end_date: # loop for period of dates
        for user in users: # iterating the dictionary
            birth_date = datetime.strptime(user['birthday'], '%d.%m.%Y') # making date object from string
            if  birth_date.day == start_date.day and birth_date.month == start_date.month: 
                if start_date.weekday()<5:
                    user_birth[start_date.strftime('%A')].append(user['name'])
                else:
                    user_birth['Monday'].append(user['name'])
        start_date+=timedelta(days=1)
    return user_birth

def print_dictionary(some_dictionary):
    for key, value in some_dictionary.items():
        list_to_string_names = ', '.join(value)
        print(f'{key}: {list_to_string_names}')

def main():
    users = [{'name':'Jack', 'birthday':'17.05.1985'},
        {'name':'John', 'birthday':'18.05.1987'},
        {'name':'Ella', 'birthday':'18.05.1986'},
        {'name':'Fiji', 'birthday':'19.05.1988'},
        {'name':'Kate', 'birthday':'21.05.1989'},
        {'name':'Mike', 'birthday':'21.05.1989'},
        {'name':'Bill', 'birthday':'23.05.1989'},
        {'name':'Eve', 'birthday':'26.05.1989'},
        {'name':'Jane', 'birthday':'23.05.1989'},
        {'name':'Heather', 'birthday':'24.05.1989'},
        {'name':'Brandon', 'birthday':'25.05.1989'},
        {'name':'Bruce', 'birthday':'27.05.1989'}]
    print(print_dictionary(congratulate(users)))    

if __name__ == '__main__':
    main()
    
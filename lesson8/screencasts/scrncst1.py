from datetime import datetime

def main():
    user_input = input('Enter datetime in format dd.mm |-|:')
    user_entered_date = datetime.strptime(user_input, '%d.%m')
    current_date = datetime.now()
    user_entered_date = user_entered_date.replace(year = current_date.year)
    if current_date>user_entered_date:
        user_entered_date = user_entered_date.replace(year = current_date.year+1)
    target_date_string = datetime.strftime(user_entered_date, '%d %B')
    delta = user_entered_date-current_date
    print(f'{delta.days} days left till {target_date_string}')
    print(f'{delta.seconds} days left till {target_date_string}')
    

if __name__ == '__main__':
    main()
import random
from datetime import datetime, timedelta

def main():
    starting_date = input('Enter starting date: ')
    end_date = input('Enter ending date: ')

    starting_date = datetime.strptime(starting_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    inerval_days = (end_date - starting_date).days
    days_delta = random.randint(0, inerval_days + 1)
    print(starting_date + timedelta(days=days_delta))


if __name__ == '__main__':
    main()

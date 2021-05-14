from datetime import datetime


def get_days_from_today(date):
    current_date = datetime.now()
    entered_date = datetime.strptime(date, "%Y-%m-%d")
    interval_days = (current_date - entered_date).days
    return interval_days

print(get_days_from_today("2021-05-21"))
# 27.List all Mondays in a given month

from datetime import date, timedelta

def list_mondays(year, month):
    mondays = []
    current = date(year, month, 1)
    while current.weekday() != 0:
        current += timedelta(days=1)
    while current.month == month:
        mondays.append(current)
        current += timedelta(days=7)
    return mondays

for monday in list_mondays(2025, 6):
    print(monday)

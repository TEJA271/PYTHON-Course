# 22.Convert string to datetime

from datetime import datetime

date_string = input("Enter a date and time (e.g., 2025-06-06 14:30): ")

date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M")

print(f"The datetime object is: {date_object}")

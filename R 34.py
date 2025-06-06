# 34.Generate Random Date Between Two Dates

import random
from datetime import datetime, timedelta

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

print(random_date(start_date, end_date).date())

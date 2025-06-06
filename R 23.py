#23.Add and subtract time

from datetime import datetime, timedelta

now = datetime.now()
print("Current time:", now)

added_time = now + timedelta(hours=2, minutes=30)
print("After adding 2 hours 30 minutes:", added_time)

subtracted_time = now - timedelta(days=1, minutes=45)
print("After subtracting 1 day 45 minutes:", subtracted_time)

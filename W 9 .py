#9.Countdown Timer in Python



import time

t = int(input("Seconds: "))
while t > 0:
    print(t)
    time.sleep(1)
    t -= 1
print("Done!")

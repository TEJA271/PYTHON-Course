#5. Simple Stopwatch 
#A stopwatch is a fun project that teaches you how to work with time in Python. Just like a normal basic stopwatch, where you can start, or stop time accordingly, you can create the same with basic Python commands.


import time

print("Simple Stopwatch")
print("Press ENTER to start")
input() 

start_time = time.time()
print("Stopwatch started... Press ENTER to stop")

input()  
end_time = time.time()

Completed_time = end_time - start_time

print(f"Completed time: {Completed_time:.2f} seconds")

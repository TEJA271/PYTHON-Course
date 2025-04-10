# 6. Write a Python program that asks for a number and tells if it is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
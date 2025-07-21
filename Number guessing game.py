import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    guess = int(input("Wrong! Try again: "))
print("Correct! 🎉")

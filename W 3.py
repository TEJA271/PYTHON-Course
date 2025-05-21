
#3. Dice Rolling Simulator
#In this project, you can simulate the rolling of a dice. Now every time you or any player runs the problem, they# will land on a certain number from 1 – 6. It’s a simple project that helps you work with random numbers in Python.






import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print(" Welcome to the Dice Rolling Simulator! ")
    while True:
        input("Press Enter to roll the dice... ")
        result = roll_dice()
        print(f"You rolled a {result}!")

        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

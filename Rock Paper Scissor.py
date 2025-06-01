import random

options = ["ROCK","PAPER","SCISSORS"]

user_choice = input("Choose ROCK , PAPER OR SCISSORS :   ")

computer_choice = random.choice(options)

print ("You have chose ",user_choice)

print ("comuter have chose  ",computer_choice)

if user_choice == computer_choice:
    
    print("its a tie")

elif user_choice == "ROCK" and computer_choice == "SCISSORS":
    
    print("ROCK smashes scissors !! you win ")

elif user_choice == "SCISSORS" and computer_choice == "PAPER":
    
    print("Scissors cut PAPER !! you win ")

elif user_choice == "PAPER" and computer_choice == "ROCK":
    
    print("PAPER covers Rock !! you win ")

else:
    print("you lose")
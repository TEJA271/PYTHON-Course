answer = input("Is Sydney the capital of Australia? (y/n): ")

if answer.lower() == 'y':
    print("Wrong! Canberra is the capital!")
elif answer.lower() == 'n':
    print("Correct!")
else:
    print("I do not understand your answer!")
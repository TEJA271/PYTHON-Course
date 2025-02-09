def check_clothing_suggestion(temp):
    if temp < 20:
        return "Wear a jacket!"
    else:
        print("You can wear light clothes!")

        
temp = int(input("Enter the temperature in °C: "))
print(check_clothing_suggestion(temp))

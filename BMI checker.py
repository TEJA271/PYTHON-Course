height =float(input("enter your height in cm :"))
weight =float(input("enter your weight in kg :"))
BMI =weight/(height/100)**2
print("your BMI is ",BMI)
if BMI <=18.4:
    print("You are under weight .")
elif BMI <=24.9:
    print ("you are healthy")
elif BMI <=29.9:
    print("you are over weight .")
elif BMI<=34.9:
    print("You are severely over weigt .")
elif BMI<=39.9:
    print("you are obese .")
else:
    print("you are severely obese .")
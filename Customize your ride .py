print("Choose your ride")
print("1. Bike")
print("2. Car")

choice = int( input("Enter your choice: ") )
 
if( choice == 1 ):
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")

  choice2=int(input("Enter you choice2: "))
  if choice2==1: 
    print("you have selected scooty")
    print("good Choice!!")
  else:
    print("you have selected scooter")
    print("good Choice!!")

elif( choice == 2 ): 
  print( "what type of car?" )
  print("1.Sedan")
  print("2.XUV")
  choice3=int(input("enter your choice3: "))
  if choice3==1: 
    print("you have selected sedan")
    print("good Choice!!")
  else:
    print("you have selected XUV")
    print("Great Choice !!")

else: 
  print("Wrong choice!")














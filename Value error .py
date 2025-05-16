try:
    number = int(input("enter a numer: "))
    print("the number enter is ", number)
except  ValueError as ex:
    print("Expetion ",ex)
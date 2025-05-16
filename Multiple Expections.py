try:
    num1,num2 = eval(input("enter 2 numbers , separeted by a comma :"))
    result = num1 / num2
    print("Result is ",result)
except ZeroDivisionError :
    print("Division by  0 is error !!!!")
except SyntaxError :
    print("comma is missing. enter numbers separated by comma like this 1, 2")
except:
    print ("Wrong input")
else: 
    print("Print no exeptions")
finally:
    print("this will excute no matter what")
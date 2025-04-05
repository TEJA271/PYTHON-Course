#13. Write a program to print numbers in the reverse order.
number = input("please enter your own number which is 4 character long or above :")

number2 = ("")
for n in number :
    number2 = n+number2

print("the Original number is",number)
print("the reversed number is ",number2)
actual_cost=float(input("Please enter the actual cost price : "))
sale_amount=float(input("enter the sales amount :"))

if(sale_amount>actual_cost):
    profit=sale_amount-actual_cost
    print(profit)
else:
    print("No profit")
    
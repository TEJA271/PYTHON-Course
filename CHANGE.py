total_cost = float(input("Enter the total cost $: "))
amount_paid = float(input("Enter the amount paid $: "))

change = amount_paid - total_cost

print("Change to return: $", round(change, 2))

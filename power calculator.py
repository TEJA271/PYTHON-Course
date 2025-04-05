num = int(input("Enter a number: "))
n = int(input("How many powers to calculate? "))

for i in range(1, n + 1):
    print(f"{num}^{i} = {num**i}")
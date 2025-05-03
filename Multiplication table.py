def print_multiplication_table(num, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(number)

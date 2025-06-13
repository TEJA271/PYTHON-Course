n = int(input("Enter a number: "))

odd_numbers = [i for i in range(n) if i % 2 != 0]

even_numbers = [i for i in range(n) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated fruit list:", capitalized_fruits)

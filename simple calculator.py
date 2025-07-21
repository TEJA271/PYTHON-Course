count = int(input("How many numbers do you want to calculate? : "))
operator = input("Enter the operator (+, -, *, /): ")

if operator not in ['+', '-', '*', '/']:
    print("Invalid operator.")
else:
    numbers = []

    for i in range(count):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    result = numbers[0]

    for num in numbers[1:]:
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        elif operator == '/':
            if num != 0:
                result /= num
            else:
                print("Error: Division by zero.")
                break

    else:  
        print("Result:", result)

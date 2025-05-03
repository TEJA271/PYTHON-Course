def swap_three_values(a, b, c):
    return c, a, b

a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
print(*swap_three_values(a, b, c))
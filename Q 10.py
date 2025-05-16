#10.Write a Python function to check whether a number falls within a given range

# Check if a number is within a range
num = int(input("Enter a number: "))
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print(start_range <= num <= end_range)
lower = int(input("enter a hiher range :"))
higher = int(input("enter a lower range :"))

print("the prime numbers from ",lower,"and",higher,"are :")
for num in range(lower , higher + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
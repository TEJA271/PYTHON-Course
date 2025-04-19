#upper part
Rowsize = int(input("Enter the number of rows : "))
if Rowsize%2 ==0:
    halfDiamRow = int (Rowsize/2)
else:
    halfDiamRow = int (Rowsize/2)+1
space = halfDiamRow-1
for i in range(1,halfDiamRow + 1):
    for j in range(1, space + 1):
        print(end=' ')
    space = space-1
    num =1
    for j in range(2*i-1):
        print(end=str(num))

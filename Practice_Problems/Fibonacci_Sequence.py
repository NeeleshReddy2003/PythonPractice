n = int(input("Enter how many numbers to be printed "))
a, b = 0, 1
for i in range(0, n):
    c = a+b
    a, b = b, c
    print(c, end=" ")

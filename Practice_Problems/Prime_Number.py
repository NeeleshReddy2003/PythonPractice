n = int(input())
count = 0
for i in range(1, n):
    if n % i == 0:
        count = count + 1
if count == 1:
    print("Prime Number")
else:
    print("Not a Prime Number")

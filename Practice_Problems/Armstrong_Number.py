n = int(input())
z = len(str(n))
temp = n
summ = 0
while temp > 0:
    ele = temp % 10
    summ = (ele ** z) + summ
    temp = temp // 10
if n == summ:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

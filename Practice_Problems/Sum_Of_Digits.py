n = int(input())
summ = 0
while n > 0:
    summ = summ + (n % 10)
    n //= 10
print(summ)

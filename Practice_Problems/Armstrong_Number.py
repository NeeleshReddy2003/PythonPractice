n=int(input())
l=len(str(n))
temp=n
sum=0
#print(l)
while temp > 0:
    ele=temp%10
    sum=(ele**l)+sum
    temp=temp//10
if(n==sum):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

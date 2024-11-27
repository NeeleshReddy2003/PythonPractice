arr=[]
n=int(input("No of Elements "))
for i in range(0,n):
    a=int(input())
    arr.append(a)
arr.sort()
print("Largest Element is ", arr[n-1])
print("Smallest Element is ", arr[0])
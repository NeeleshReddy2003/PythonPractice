arr = []
n = int(input("Enter array size "))
for i in range(0, n):
    a = int(input())
    arr.append(a)
arr.sort()

arr2 = []
i = 0
while i < n-1:
    if arr[i] != arr[i+1]:
        b = arr[i]
        arr2.append(b)
#       arr.remove(i+1)
    i = i+1
d = len(arr2)
for j in range(0, d):
    print(arr2[j], end=" ")

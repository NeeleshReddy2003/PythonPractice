n=input("Enter String ")
c,v=0,0
vowels='aeiouAEIOU'
for i in n:
    if i in vowels:
        v+=1
    elif i==' ':
        continue
    else:
        c+=1
print(c,v)
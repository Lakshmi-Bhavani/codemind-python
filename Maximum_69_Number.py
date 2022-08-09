num=input()
#print(num)
num=list(num)
s=""
for i in range(0,len(num)):
    a=num[i]
    #print(a,end=" ")
    if a=="6":
        num[i]="9"
        break
for i in num:
    s+=i
print(s)


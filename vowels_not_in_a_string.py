s=input()
l=list(s)
lis=["a","e","i","o","u"]
l1=[]
l2=[]
for i in range(0,len(l)):
    x=l[i]
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        l1.append(x)
for i in lis:
    if i not in l1:
        l2.append(i)
if len(l2)>0:
    for j in l2:
        print(j,end=" ")
else:
    print("0")
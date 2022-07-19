s=list(input())
l=[]
for i in range(0,len(s)):
    x=s[i]
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        if x not in l:
            l.append(x)
if len(l)>0:
    for j in l:
        print(j,end=" ")
else:
    print("-1")

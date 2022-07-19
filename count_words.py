s=input()
x=""
l=[]
lis=["a","e","i","o","u","A","E","I","O","U"]
count=0
for i in range(0,len(s)):
    a=s[i]
    if a!=" ":
        x+=a
    if a==" " or i==len(s)-1:
        l.append(x)
        x=""
for i in l:
    m=i
    v=m[0]
    c=m[-1]
    if v in lis:
        if c not in lis:
            count+=1
print(count)
    
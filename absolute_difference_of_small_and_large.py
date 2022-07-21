s=input()
x=""
l=[]
for i in range(0,len(s)):
    a=s[i]
    if a!=" ":
        x+=a
    if a==" " or i==len(s)-1:
        m=x#print(m)
        for j in range(0,len(m)):
            b=ord(m[j])
            l.append(b)
            mi=(min(l))
            ma=(max(l))
        res=ma-mi
        print(res,end=" ")
        l=[]
        x=
s=input()
x=''
l=[]
l1=[]
l2=[]
for i in range(0,len(s)):
    a=s[i]
    if a!=" ":
        x+=a
    if a==" " or i==len(s)-1:
        l.append(x)
        x=""
#print(l)
for i in range(0,len(l)):
    y=list(l[i])
    #print(y)
    for j in y:
        l1.append(ord(j))
    #print(l1)
    mi=min(l1)
    ma=max(l1)
    l1=[]
    #print(mi,ma)
    print(chr(mi),chr(ma),end=" ")
    
    
    
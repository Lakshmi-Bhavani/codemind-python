s=input()
#print(s)
x=""
l=[]
l1=[]
mi=0
ma=0
for i in range(0,len(s)):
    a=s[i]
    if a!=" ":
        x+=a
    if a==" " or i==len(s)-1:
        l.append(x)
        x=""
#print(l)
for i in range(0,len(l)):
    m=l[i]
    #print(m)
    for j in range(0,len(m)):
        y=ord(m[j])
        l1.append(y)
        #print(l1)
    mi+=min(l1)
    ma+=max(l1)
    l1=[]
print(ma-mi)
        
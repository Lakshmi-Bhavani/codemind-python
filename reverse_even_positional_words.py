s=input()
temp=s
x=""
y=""
l=[]
l2=[]
for i in range(0,len(temp)):
    b=temp[i]
    if b!=" ":
        y+=b
    if b==" " or i==len(temp)-1:
        l2.append(y)
        y=""
for i in range(1,len(s)+1):
    a=s[-1*i]
    if a!=" ":
        x+=a
    if a==" " or i==len(s):
        l.append(x)
        x=""
l.reverse()
for i in range(0,len(l2),2):
    l2[i]=l[i]
for i in l2:
    print(i,end=" ")
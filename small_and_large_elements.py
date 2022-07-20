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
m=list(l[0])
n=list(l[-1])
for i in m:
    l1.append(ord(i))
y=min(l1)
res1=chr(y)
for i in n:
    l2.append(ord(i))
z=max(l2)
res2=chr(z)
print(res1,res2)
s=input()
#print(s)
s.split()
x=""
l=[]
for i in range(0,len(s)):
    a=s[i]
    if a!=" ":
        x+=a
    if a==" ":
        l.append(x)
        x=""
    if i==len(s):
        break
print(x,end=" ")
l.reverse()
for i in range(0,len(l)):
    m=l[i]
    print(m,end=" ")
    
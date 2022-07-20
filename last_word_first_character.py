s=input()
#print(s)
x=""
l=[]
for i in range(0,len(s)):
    a=s[i]
    if a!=" ":
        x+=a
    if a==" " or i==len(s)-1:
        l.append(x)
        x=""
#print(l)
m=l[-1]
print(m[0])
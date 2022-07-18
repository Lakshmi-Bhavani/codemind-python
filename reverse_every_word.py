s=input()
x=""
l=[]
for i in range(1,(len(s)+1)):
    a=s[-1*i]
    if a!=" ":
        x+=a
    if a==" " or i==len(s):
        l.append(x)
        x=""
#print(x,end=" ")
l.reverse()
for i in range(0,len(l)):
    m=l[i]
    print(m,end=" ")

    
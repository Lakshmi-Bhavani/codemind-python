s=input()
#print(s)
x=""
z=0
v=["a","e","i","o","u","A","E","I","O","U"]
for i in range(0,len(s)):
    a=s[i]
    if a!=" ":
        x+=a
    if a==" " or i==len(s)-1:
        m=x
        #print(m)
        for i in range(0,len(m)//2):
            c=m[i]
            d=m[len(m)-1-i]
            #print(c,d)
            if (c in v and d not in v) or (c not in v and d in v):
                z+=1
    
        x=""
print(z)
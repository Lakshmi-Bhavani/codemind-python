s=input()
l=list(s)
#print(l)
c=0
v=["a","e","i","o","u","A","E","I","O","U"]
for i in range(0,(len(l)//2)):
    a=l[i]
    b=l[len(l)-1-i]
    #print(a,b)
    if (a in v and b not in v and b!=" ") or (a not in v and a!=" " and b in v):
        c+=1
        #print(c)
print(c)
    
    

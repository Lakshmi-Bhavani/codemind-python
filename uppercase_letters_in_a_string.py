s=input()
l=list(s)
c=0
for i in range(0,len(s)):
    x=l[i]
    if(x.isupper()):
        c+=1
    #print(c)
print(c)
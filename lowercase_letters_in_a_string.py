s=input()
c=0
for i in range(0,len(s)):
    x=s[i]
    if(x.islower()):
        c+=1
print(c)
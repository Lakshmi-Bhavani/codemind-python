s=input()
s=list(s)
c=0
for i in range(0,len(s)):
    if s[i]==" " or i==len(s)-1:
        c+=1
print(c)
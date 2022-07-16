s=list(input())
c=0
for i in range(0,len(s)):
    if s[i]==" ":
        c-1
    c+=1
    if i==len(s)-1:
        break
print(c)
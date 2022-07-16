s=list(input())
c=0
l=[]
for i in range(0,len(s)):
    if s[i]!=" ":
        c+=1
    if s[i]==" " or i==len(s)-1:
        print(c,end=" ")
        c=0
        
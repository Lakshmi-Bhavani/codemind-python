s=input()
c1=0
c2=0
for i in range(0,len(s)):
    x=s[i]
    if(x.isalpha()):
        c1+=1
    if x==" ":
        c2+=1
print(len(s)-c1-c2)
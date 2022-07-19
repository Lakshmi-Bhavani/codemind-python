s=list(input())
#print(s)
c=0
l=[]
for i in range(0,len(s)):
    x=s[i]
    if x!=" ":
        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
            c+=1
    if x==" " or i==len(s)-1:
        l.append(c)
        c=0
r=(max(l))
print(l.count(r))
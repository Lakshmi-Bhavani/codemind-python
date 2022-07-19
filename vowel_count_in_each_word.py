s=input()
#print(s)
c=0
l=[]
#print(len(s))
for i in range(0,len(s)):
    #print(i)
    x=s[i]
    if x!=" ":
        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
            c+=1
           # print(c)
    if x==" " or i==len(s)-1:
        l.append(c)
        c=0
#print(l)
for i in l:
    print(i,end=" ")
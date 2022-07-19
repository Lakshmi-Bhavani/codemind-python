s=input()
c=0
for i in range(0,len(s)):
    x=s[i]
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        c+=1
print(c)        
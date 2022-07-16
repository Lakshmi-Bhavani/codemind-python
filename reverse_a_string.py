s=input()
l1=[]
m=""
l=list(s)
for i in range(1,len(s)+1):
    x=s[-1*i]
    l1.append(x)
for i in range(0,len(l1)):
    m=m+l1[i]
print(m)
n=int(input())
l=list(map(int,input().split()))
x=0
m=0
for i in l:
    a=l.count(i)
    l.remove(i)
    if a==i:
        x+=i
        m+=1
if m==0:
    print("-1")
else:
    res=x/m
    print("%.2f"%res)

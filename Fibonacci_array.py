n=int(input())
l=list(map(int,input().split()))
s=l[0]+l[1]
f=0
for i in range(0,n-2):
    x=l[i]
    y=l[i+1]
    if x+y==l[i+2]:
        f=1
    else:
        f=0
        break
if f==0:
    print("no")
else:
    print("yes")
    
    
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n):
    a=l[i-1]
    b=l[i]
    if b>a:
        c+=1
if c==0:
    print("yes")
else:
    print("no")
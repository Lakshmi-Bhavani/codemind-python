n=int(input())
l=list(map(int,input().split()))
l2=[]
for i in range(0,n):
    a=l[i]
    b=len(str(a))
    l2.append(b)
x=max(l2)
for i in range(0,n):
    y=l[i]
    if len(str(y))==x:
        print(y,end=" ")
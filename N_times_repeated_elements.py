n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
for i in l:
    a=l.count(i)
    if a==k and i not in l1:
        l1.append(i)
if len(l1)!=0:
    for i in l1:
        print(i,end=" ")
else:
    print(-1)
    
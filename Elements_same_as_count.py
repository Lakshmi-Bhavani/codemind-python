n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in l:
    a=l.count(i)
    if a==i and i not in l1:
        l1.append(i)
if len(l1)!=0:
    for j in l1:
        print(j,end=" ")
else:
    print(-1)
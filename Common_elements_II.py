a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l2:
    l1.append(i)
for i in l1:
    if l1.count(i)==1:
        print(i,end=" ")
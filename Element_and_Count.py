n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    a=l.count(i)
    print(i,a,end=" ")
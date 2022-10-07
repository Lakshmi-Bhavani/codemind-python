n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
for i in range(a,b):
    if i in l:
        l1.append(i)
if len(l1)>0:
    print(min(l1))
else:
    print(-1)
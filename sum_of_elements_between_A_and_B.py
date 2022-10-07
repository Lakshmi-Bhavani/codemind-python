n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
for i in range(a,b+1):
    if i in l:
        l1.append(i)
print(sum(l1))
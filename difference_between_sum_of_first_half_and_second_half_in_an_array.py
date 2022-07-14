n=int(input())
l=list(map(int,input().split()))
res1=0
res2=0
res=0
for i in range(0,n//2):
    res1+=l[i]
for j in range(n//2,n):
    res2+=l[j]
res=res2-res1
print(res)
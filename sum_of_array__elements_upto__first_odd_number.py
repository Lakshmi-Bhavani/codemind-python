n=int(input())
l=list(map(int,input().split()))
res=0
for i in range(0,n):
    x=l[i]
    if x%2==0:
        res+=x
    else:
        break
print(res)
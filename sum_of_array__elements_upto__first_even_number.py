n=int(input())
l=list(map(int,input().split()))
res=0
for i in range(0,n):
    a=l[i]
    if a%2!=0:
        res+=a
    else:
        break
print(res)
def xxx(x):
    y=0
    while x:
        rem=x%10
        x=x//10
        y+=rem
    return y
n=int(input())
l=list(map(int,input().split()))
res=0
for i in range(0,n):
    a=xxx(l[i])
    res+=a
print(res)
n=int(input())
l=list(map(int,input().split()))
#print(l)
for i in range(0,n):
    a=l[i]
    if a<0:
        a=-1*a
    b=len(str(a))
    print(b,end=" ")
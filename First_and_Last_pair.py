n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)//2):
    a=l[((i+1)*-1)]
    print(l[i],a,end=" ")
if n%2!=0:
    print(l[n//2],0)

    
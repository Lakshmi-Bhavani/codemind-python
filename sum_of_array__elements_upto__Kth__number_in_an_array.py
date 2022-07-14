n=int(input())
l=list(map(int,input().split()))
k=int(input())
#print(l)
#print(k)
res=0
for i in range(0,n):
    a=l[i]
    #print(a,end=" ")
    if a!=k:
        res+=a
        #print(res)
    if a==k:
        break
print(res+k)
    
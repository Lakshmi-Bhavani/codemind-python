n,k=map(int,input().split())
#print(n,k)
l=list(map(int,input().split()))
#print(l)
c=0
for i in range(0,n):
    a=l[i]
    if a<0:
        a=-1*a
    if len(str(a))==k:
        c+=1
    #print(a,c)
print(c)
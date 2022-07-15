n=int(input())
l=list(map(int,input().split()))
#print(l)
l2=[]
for i in range(0,n):
    a=l[i]
    b=len(str(a))
    #print(a,b)
    l2.append(b)
x=min(l2)
print(l2.count(x))
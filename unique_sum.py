n=int(input())
l=list(map(int,input().split()))
x=[]
for i in range(0,len(l)):
    a=l.count(l[i])
    if l[i] not in x:
            x.append(l[i])
print(sum(x))
    
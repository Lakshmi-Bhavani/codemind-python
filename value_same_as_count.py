n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    a=l.count(i)
    if i==a:
        x.append(a)
        l.remove(i)
print(len(x))
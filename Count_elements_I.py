n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
l1=[]
l2=[]
for i in x:
    if i not in l1:
        l1.append(i)
for j in y:
    if j not in l2:
        l2.append(j)
c=0
for i in l1:
    if i in l2:
        c+=1
print(c)
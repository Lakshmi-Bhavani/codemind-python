n=int(input())
l=list(map(int,input().split()))
#l.sort()
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
m=min(len(l1),len(l2))
for i in range(0,m):
    print(l2[i],l1[i],end=" ")
if m==len(l1):
    for j in range(m,len(l2)):
        print(l2[j],end=" ")
else:
    for j in range(m,len(l1)):
        print(l1[j],end=" ")
if n%2!=0:
    print(0)

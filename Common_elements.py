a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
l=[]
for i in l1:
    if i in l2:
        l3.append(i)
for i in l3:
    if i not in l:
        l.append(i)
for i in l:
    print(i,end=" ")

        
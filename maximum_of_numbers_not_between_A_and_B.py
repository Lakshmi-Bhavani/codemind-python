num=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
c=0
for i in range(0,num):
    if l[i]<a or l[i]>b:
        d.append(l[i])
        c+=1
if c==0:
    print("-1")
else:
    print(max(d))
        
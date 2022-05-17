num=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in range(0,num):
    if l[i]<a or l[i]>b:
        c+=1
        print(l[i],end=" ")
if c==0:
    print("-1")

        
        
n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l),2):
    a=l[i]
    b=l[i+1]
    for j in range(0,b):
        print(a,end=" ")
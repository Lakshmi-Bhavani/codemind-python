import math
def isprime(x):
    if x==1 or x==0:
        return 0
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return 0
        return 1
    
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i>1:
        res=isprime(i)
        if res==1:
            c+=1
print(c)
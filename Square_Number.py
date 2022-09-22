import math as m
n=int(input())
x=int(m.sqrt(n))
temp=0
for i in range(0,x+1):
    for j in range(0,x+1):
        if ((i*i)+(j*j))==n:
            temp=1
           
if temp==0:
    print("False")
else:
    print("True")
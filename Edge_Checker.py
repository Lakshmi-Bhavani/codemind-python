a,b=map(int,input().split())
if a<b:
    a,b=b,a
if a==10 and b==1:
    print("Yes")
elif a==b+1:
    print("Yes")
else:
    print("No")
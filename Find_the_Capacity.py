s,t,b=map(int,input().split())
c=2*s*t*b*512
c=c//1024
c=str(c)
d="KB"
print(c+d)
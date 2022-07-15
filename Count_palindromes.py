def palindrome(x):
    temp=x
    rev=0
    while x:
        rem=x%10 #1 2 1   9 8 7
        x=x//10
        rev=(rev*10)+rem
    if rev==temp:
        return 1
    else:
        return 0
n=int(input())
l=list(map(int,input().split()))
res=0
for i in range(0,n):
    a=palindrome(l[i])
    if a==1:
        res+=1
print(res)
    
        
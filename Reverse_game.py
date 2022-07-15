def palindrome(x):
    rev=0
    while x:
        rem=x%10
        x=x//10
        rev=rev*10+rem
    return rev
n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    a=palindrome(l[i])
    print(a,end=" ")
    
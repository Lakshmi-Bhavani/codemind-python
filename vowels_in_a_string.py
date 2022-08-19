s=input()
v=input()
c=0
for i in range(0,len(s)):
    a=s[i]
    if a==v:
        c=1
        print("True")
        print(i)
        break
if c==0:
    print("False")
s=input()
l=list(s)
l1=[]
l2=[]
cv=["A","E","I","O","U"]
sv=["a","e","i","o","u"]
for i in range(0,len(s)):
    x=l[i]
    if x in cv:
        if x not in l1:
            l1.append(x)
    if x in sv:
        if x not in l2:
            l2.append(x)
if len(l1)==len(cv) or len(l2)==len(sv):
    print("True")
else:
    print("False")
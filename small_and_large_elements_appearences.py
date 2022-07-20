s=input()
l=list(s)
#print(l)
for i in l:
    if i==" ":
        l.remove(i)
l1=[]
for i in range(0,len(l)):
    l1.append(ord(l[i]))
#print(l1)
mi=chr(min(l1))
ma=chr(max(l1))
#print(mi,ma)
res1=l.count(mi)
res2=l.count(ma)
print(mi,res1,ma,res2)
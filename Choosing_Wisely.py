v = [6, 10, 12]
c = [30, 60, 90]
mc = 200

l=list()
sum=0
while mc>0 and len(c)>0:
    m=max(c)
    i=c.index(m)
    l.append(v[i])
    c.pop(i)
    mc=mc-m

for i in l:
    sum=sum+i

print(sum)

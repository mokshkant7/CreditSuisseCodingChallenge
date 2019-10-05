scores = [100,90,90,80,75,60]
alice = [50,77,77,90]
s=[]
for a in scores:
    if a in s:
        continue
    else:
        s.append(a)
l=[]
for i in alice:
    s.append(i)
    s.sort()
    s.reverse()
    pos=s.index(i)+1
    l.append(pos)
    #print(s)
    s.remove(i)
    #print(pos)
#print(l)
m=max(l,key=l.count)
print(m)

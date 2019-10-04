print('Enter trader skills')
t=input()
T=t.split(',')
print('Enter risks')
r=input()
R=r.split(',')
print('Enter bonuses')
b=input()
B=b.split(',')
pos=0
s=0

l=list()
m=list()

for i in T:
    for j in R:
        if i>=j:
            l.append(B[pos])
        pos=pos+1
    l.sort()
    #print(l)
    m.append(l[len(l)-1])
    #print(m)
    l=[]
    pos=0

print(m)

for i in m:
    s=s+int(i)
print(s)

n=input()
a=[]
b=[]
for i in range(len(n)):
    a.append(n.count(n[i]))

for i in range(len(n)):
    b.append([n[i],a[i]])
c=[]
for i in range(len(b)):
    if (b[i] in c)==False:
        c.append(b[i])

for i in range(len(c)):
    print(str(c[i][0])+'('+str(c[i][1])+')')
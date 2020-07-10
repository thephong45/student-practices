import random
# exercise 1 
print('hello world')
# exercise 2
print('nhap ten ')
name=input()
print('hello' + name)
# exercise 3 
name=input()
if name=='Alice' or name=='Bob':
    print('hello '+name)
else:
    print('bye')
# exercise 4
n=input()
tong=0
for i in range(n+1):
    tong+=i
print(tong)
# exercise 5
n=input()
tong=0
for i in range(n+1):
    if i%3==0 or i%5==0:
        tong+=i
print(tong)
# exercise 6
#import random
import random
a=random.randint(0,5)
i=[]
while True:
    n=input()
    n=int(n)
    if n>a:
        print('lon hon')
        if (n in i)==False:
            i.append(n)
    if n<a:
        print('nho hon')
        if (n in i)==False:
            i.append(n)
    if n==a:
        print('dung roi')
        break
print('so lan doan khac nhau '+str(len(i)))

# exercise 7
n=input()
n=list(n)
so=[]
chu=[]
print(n)
for i in range(len(n)):
    n[i]=ord(n[i])
    if n[i]>=97:
        chu.append(n[i])
    else:
        so.append(n[i])
n=chu+so
print(''.join(chr(i) for i in n))
# excercise 8
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
# excercise 9
a=[]
i=2020
while i>2019:
    if i%4==0 and i%100!=0:
        a.append(i)
    if len(a)==20:
        break
    i+=1
print(a)

# excercise 10
import math
a=int(input())
b=int(input())
c=int(input())
denta=b*b-4*a*c
if denta<0:
    print('vo nghiem')
if denta>=0:
    x1=-b+math.sqrt(denta)/(2*a)
    x2=-b-math.sqrt(denta)/(2*a)
    if x1==x2:
        print(x1)
    else:
        print(x1,x2)
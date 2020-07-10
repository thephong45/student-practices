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
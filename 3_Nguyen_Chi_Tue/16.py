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
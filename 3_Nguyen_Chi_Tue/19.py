a=[]
i=2020
while i>2019:
    if i%4==0 and i%100!=0:
        a.append(i)
    if len(a)==20:
        break
    i+=1
print(a)
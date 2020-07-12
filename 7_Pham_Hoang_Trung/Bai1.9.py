def Leap_year(year):
    if((year%4==0 and year%100!=0) or year % 400 == 0):
        return True

count = 0
year = 2020
array =[]
while(count<20):
    if(Leap_year(year)==True):
        array.append(year)
        #print(count)
        count +=1
    #print(year)
    year +=1

for i in array:
    print("{}".format(i))







start=1
print("Please input your number")
end=int(input())
sum=0
for i in range(start,end+1):
    sum=sum+i
print("Sum from 1 to {} is {}".format(end,sum))
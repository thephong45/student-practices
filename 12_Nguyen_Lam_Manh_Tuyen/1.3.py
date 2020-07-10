names=["Alice","Bob"]
print("Please input your name")
name=input()
while name not in names:
    print("Please input your name")
    name = input()
    if name=="Alice":
        print("Hello",name)
    elif name=="Bob":
        print("Hello",name)

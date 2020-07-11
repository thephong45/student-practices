# Modify the previous program such that only the users Alice and Bob are greeted with their names.

while 1:
    a = input("nhap vao ten cua ban: ")
    if(a=="Alice" or a =="Bod"):
        print("xin chao " + a)
        break
    else:
        print("ban nhap sai ten, vui long nhap lai ten")
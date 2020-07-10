# Order the input string by ASC (a -> z, 0 -> 9) with any string

a = input("nhap vao chuoi: ")
b = ''.join(sorted(str(a)))
print("chuoi sau khi sap xep: " + str(b))
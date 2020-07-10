# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n


tong = 0
n = input("nhap vao so n: ")
for x in range(int(n)):
    tong += x
txt = "tong cac so tu 1 den n la: {}"
print(txt.format(tong + int(n)))
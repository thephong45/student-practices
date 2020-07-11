# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.


sobimat = 1117
while 1:
    a = int(input("nhap vao so: "))
    if(a == sobimat):
        print("ban doan dung roi !")
        break
    else:
        print("ban doan sai roi! ")

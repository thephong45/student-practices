import random
lov=[]
secretnum=random.randrange(1,100)
print(secretnum)
guess=()
while guess!=secretnum:
    print("Please input your guess")
    guess = int(input())
    if guess<secretnum:
        print("Your input number is lower than the secret number")
    if guess>secretnum:
        print("Your input number is higher than the secret number")
    if guess==secretnum:
        #count times user have tried to input
        lov=list(set(lov))
        count=len(lov)+1
        print("Bingo, You've guessed it correcly in {} times".format(count))
    lov.append(guess)


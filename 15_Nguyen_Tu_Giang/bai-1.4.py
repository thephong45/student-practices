# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

print('What is your number?')
value = input()
i = 1
result = 0
while i <= int(value):
    result += i
    i += 1
    print(result)

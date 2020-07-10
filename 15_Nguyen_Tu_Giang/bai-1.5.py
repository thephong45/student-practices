# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

print('What is your number?')
value = input()
i = 3
result = 0
while i <= int(value):
    if i % 5 == 0:
        result += int(i / 5)
    elif i % 3 == 0:
        result += int(i / 3)
    i += 1
print(result)



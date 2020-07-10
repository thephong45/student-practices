# Modify the previous program such that only the users Alice and Bob are greeted with their names.

print('What is your name?')
value = input()
if value == 'Alice' or value == 'Bob':
    print('Hello,', value)
else:
    print("Hello guest!")

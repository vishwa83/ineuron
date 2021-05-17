'''
Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

count = 2
for i in range(10):
    if i <= 5:
        num = '* ' * i
        print(num)
    elif i >= 6:
        num = '* ' * (i - count)
        print(num)
        count += 2

'''Write a Python program to reverse a word after accepting the input from the user.'''

word = input("Please type a word of your choice (only one word) ")
word_list = list(word)
print(''.join(word_list[::-1]))

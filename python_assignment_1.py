"""
1. Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line
"""

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=",")


"""
2. Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name

"""
fname, lname = input(
    "Please type your name in the following format - First Name, Last Name "
).split(",")
print(f"Welcome to ineuron MR. {lname.title()} {fname.title()}")


"""
3. Write a Python program to find the volume of a sphere with diameter 12 cm
Formula: V=4/3 * π * r 3
"""


def find_volume(diameter):
    pi = 3.14
    radius = diameter / 2
    volume = 4 / 3 * pi * radius ** (1 / 3)
    print(volume)


find_volume(12)

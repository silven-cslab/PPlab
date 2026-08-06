"""
    This python program takes a string from the user.
    Finds out the length of the string.
"""

string = input("Enter any string: ")

length = 0

for i in string:
    length += 1

print(f"The length of the string {string} is: {length}")

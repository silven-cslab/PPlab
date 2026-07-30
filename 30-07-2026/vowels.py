"""
    This python program takes a string from the user and checks the no. of vowels of the string.
"""

VOWELS = "AEIOUaeiou"
string = input("Enter any string: ")

vowelCount = 0
for char in string:
    if char in VOWELS:
        vowelCount += 1

print(f"The no .of vowels of the given string: {string} are: {vowelCount}")

"""
    This python program prints the multiplication table of the given number upto 10 steps.
"""


NUM = int(input("Enter any number: "))

print(f"The multiplication table of {NUM} is: ")

for i in range(1, 10 + 1):
    print(f"{NUM} x {i} = {NUM * i}")

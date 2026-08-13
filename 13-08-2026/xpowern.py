"""
    This python program takes a number x and it's exponent n and calucates the value.
"""


x = int(input("Enter the base x: "))
n = int(input("Enter the exponent n: "))


if(x < 1):
    print("\nInvalid base value!!\n\n")

def xpowern(x, n):
    return x ** n

print(f"\n{x} ^ {n} = {xpowern(x, n)}\n\n")

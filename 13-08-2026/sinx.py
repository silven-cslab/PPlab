"""
    This python program takes a value x and calculates sin(x).
"""

x = int(input("Enter x: "))

if(x < -1):
    print("\nInvalid value!!\n\n")

nterms = int(input("Enter the total no. of terms: "))

if(nterms < 0):
    print("\nInvalid number of terms!!\n\n")


def factorial(num):
    fact = 1
    if(num == 0 or num == 1):
        return 1

    for i in range(1, num + 1):
        fact *= i
    return fact


def xpowern(x, n):
    return x ** n


def sine(x, nterms):

    term = 0

    for t in range(nterms):
        term += (-1 ** t) * ((xpowern(x, 2* t + 1) / (factorial(2 * t + 1))))

    return term




print(f"sin({x}) = {sine(x, nterms)}\n\n")

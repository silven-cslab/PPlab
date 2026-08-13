"""
    This python program takes a value x and calculates e power x upto specified no. of terms.
"""

x = int(input("Enter x: "))

if( x < -1):
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


def ex(x, nterms):

    term = 0

    for t in range(nterms):
        term += ((xpowern(x, t) / (factorial(t))))

    return term




print(f"e^{x} = {ex(x, nterms)}\n\n")

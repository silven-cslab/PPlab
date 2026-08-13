
""" 
    This python program takes a number from the user and prints the factorial value of that number.
"""


num = int(input("Enter any number: "))

if(num < 0):
    print("\nInvalid number! Try again.")
    exit()


def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact


print(f"\nThe factorial of the given number {num} is: {factorial(num)}")

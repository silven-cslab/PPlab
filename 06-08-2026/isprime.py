
"""
    This python program takes a number from the user and checks whether the given number is prime or not.
"""

num = int(input("Enter any positive number: "))

if num < 0:
    print(f"Invalid number.")
    exit()

if num == 0 or num == 1:
    print(f"{num} is nether prime nor composite.")
    exit()

def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False

    return True

if isPrime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")

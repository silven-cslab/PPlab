
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
    SQRTnum = int(num ** 0.5)
    for PRIMES in PRIMESLIST:
        if PRIMES > SQRTnum:
            return True
        if num % PRIMES == 0:
            return False

    return True

PRIMESLIST = []
SQRTnum = int(num ** 0.5)

for s in range(2, SQRTnum + 1):
    if isPrime(s):
        PRIMESLIST.append(s)

if isPrime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")

# Prime Implementation that checks factors upto the factor that is square root of the number, except 1 and itself:

"""
    This program finds out the total no. of the primes in the range 2 to 1000.
"""

import time     # For functions that are required to calculate the execution time.


PRIMESLIST = []

def isPrime(num):
    SQRTnum = int(num ** 0.5)
    for i in PRIMESLIST:
        if i > SQRTnum:
            return True
        if num % i == 0:
            return False
    return True

start = time.perf_counter()     # start the timer

print("The Primes between 2 and 100000 are: ", end = '')
for number in range(2, 100000):
    if isPrime(number):
        print(f"{number}, ", end = '')
        PRIMESLIST.append(number)

end = time.perf_counter()       # end the timer

print(f"\nExecution Time: {end-start: .2f}")

# Execution time on Inteli5 - 12th Gen(1.30GHz): 0.07
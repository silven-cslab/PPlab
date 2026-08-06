"""

This program takes any two numbers from the user.
And, finds out the GCD of the two numbers by Euclid's algorithm.

"""


NUM1 = int(input("Enter the first number: "))
NUM2 = int(input("Enter the second number: "))

if NUM1 < NUM2:
    NUM1, NUM2 = NUM2, NUM1


while NUM2 !=0:
    remainder = NUM1 % NUM2
    NUM1 = NUM2
    NUM2 = remainder

print(f"The GCD of the given numbers is: {NUM1}")

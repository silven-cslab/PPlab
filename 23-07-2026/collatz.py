"""
Collatz Conjecture:

This conjecture states that after sequential application of the following operations on the given number:
    * If given number is EVEN : Divide the number by 2.
    * Else it is ODD: Multiply it by 3 and add 1.

And, we repeat such that at a certain number of steps the number will become 1.

In this program we take a number from the user.
Apply the sequence of the arithmetic operations on that number till 1.

Atlast, print the length of the sequence of that number.
"""


## Taking the number from the user:
num = int(input("Enter any number: "))

len_seq = 1
j = num

print("Collatz Conjecture:", num, sep = " ", end = " ")
while j!=1:
    if j %2 == 0:
        j /= 2
    else:
        j = 3 *j + 1
    len_seq += 1
    print(int(j), end = " ")


print(f"\n\nThe length of the sequence for the number {num} is: {len_seq}")

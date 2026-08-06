
"""
Collatz Conjecture:

This conjecture states that after sequential application of the following operations on the given number:
    * If given number is EVEN : Divide the number by 2.
    * Else it is ODD: Multiply it by 3 and add 1.

And, we repeat such that at a certain number of steps the number will become 1.

In this program we take a number from the user.
Apply the sequence of the arithmetic operations on that number till 1.

Atlast, print the length of the sequence of the number that has the largest length of the sequence in the specified range.
"""


## Taking the number from the user:
UPPER = int(input("Enter the upperbound(upto which number you want to check): "))

max_seq = 1
for i in range(1, UPPER + 1):
    len_seq = 1
    j = i

    while j!=1:
        if j %2 == 0:
            j /= 2
        else:
            j = 3 *j + 1
        len_seq += 1
        
    if max_seq < len_seq:
        max_seq = len_seq
        num = i


print(f"\n\nThe number {num} has the largest length of the sequence in the range (1, {UPPER}): {max_seq}")

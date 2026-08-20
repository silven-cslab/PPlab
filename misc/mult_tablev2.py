
"""

This program takes a range.
And prints the multiplication tables for all of that numbers upto 20 steps.

"""

for NUM in range(1, 21):

    loop_counter = 1

    print(f"The Multiplication table of {NUM} is: ");
    print("+--------------------------+")
    while loop_counter <= 20:
        print(f"| {NUM} x {loop_counter} = {NUM * loop_counter}")
        loop_counter += 1

    print("+--------------------------+")


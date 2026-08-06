"""
    This python program takes the size of the list.
    And, takes all of the elements that are to be inserted in the list.
    Iterates over the list and finds the total no. of even numbers in the list.
"""

MAXLIST = int(input("Enter the total no. of elements of the list: "))

LIST = []

for i in range(MAXLIST):
    Num = int(input(f"Enter the {i + 1} number: "))
    LIST.append(Num)

evenCount = 0
for Num in LIST:
    if Num % 2 == 0:
        evenCount += 1

print(f"The total no. of even numbers in the list: {LIST} is: {evenCount}");

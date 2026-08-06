"""
    This python program shows the implementation of the lists.
"""

LIST = [1, 2, 3, 4, 5, 6, 7, 8]

# first element of the list:
print(LIST[0])

#second element of the list:
print(LIST[1])

# last element of the list:
print(LIST[-1])

# second last element of the list:
print(LIST[-2])

# first 3 elements of the list:
print(LIST[:4])

print(LIST[2:4])

print(2 in LIST)

sum = 0
# Sum of all numbers:
for num in LIST:
    sum += num

print(f"The sum of all elements of the list: {LIST} is: {sum}")

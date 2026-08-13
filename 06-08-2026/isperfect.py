
""" 
    This python program takes a number from the user and applies a sequence of operations to check whether a given number is a perfect number or not.

"""


num = int(input("Enter any number: "))

if num <= 0:
    print("Invalid number!!")
    exit()

def is_perfectnumber(num):
    sumoffacts = 1

    for i in range(2, int(num+1/2)):
        if num % i == 0:
            sumoffacts += i

    if num == sumoffacts:
        return True
    else:
        return False


if is_perfectnumber(num):
    print(f"The number {num} is a perfect number.")
else:
    print(f"The number {num} is not a perfect number.")

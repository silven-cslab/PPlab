
""" 
    This python program prints all of the perfect number within a range.

"""


UPPER = int(input("Enter UPPER bound: "))

if UPPER <= 0:
    print("Invalid number!!")
    exit()

def is_perfectnumber(num):
    sumoffacts = 1

    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            sumoffacts += i

    if num == sumoffacts:
        return True
    else:
        return False


print(f"The Perfect Numbers within a range of 1 to {UPPER} are: ")
for num in range(UPPER):
    if is_perfectnumber(num):
        print(f"{num}")

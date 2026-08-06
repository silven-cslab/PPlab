
a = int(input("Enter any number: "))

b = int(input("Enter another number: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif a == b:
    print(f"{a} is equal to {b}.")
else:
    print(f"{a} is less than {b}.")

c = int(input("Enter another number: "))

if a > b and a > c:
    print(f"{a} is the largest number.")
elif b > c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")

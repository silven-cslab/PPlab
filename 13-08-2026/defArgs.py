"""
    This python program shows the implementation of the default value arguments.

"""

# printDetails():
## This function takes details like name, age, branch name, percentage of marks(default value = 0.00) and prints them.

def printDetails(name, age=18, branch="CSE", POM = 0.00):
    print(f"Name of the student: {name}")
    print(f"Age: {age}")
    print(f"Branch: {branch}")
    print(f"Percentage of marks: {POM}")


name = input("Enter the name: ")
age = int(input("Enter the age: "))
branch = input("Enter the branch: ")


printDetails(name, age, branch)
printDetails("Raakeesh", 19)
printDetails("swejo")

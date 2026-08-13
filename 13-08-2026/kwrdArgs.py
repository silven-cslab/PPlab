"""
    This python program shows the implementation of the keyword arguments.

"""

# printDetails():
## This function takes details like name, age, branch name, percentage of marks and prints them.

def printDetails(name, age = 18, branch = 'CSE', POM = 0.00):
    print(f"Name of the student: {name}")
    print(f"Age: {age}")
    print(f"Branch: {branch}")
    print(f"Percentage of marks: {POM}")


name = input("Enter the name: ")
age = int(input("Enter the age: "))
branch = input("Enter the branch: ")
POM = float(input("Enter the percentage of your marks: "))


printDetails(name, age, branch, POM)
printDetails(name = 'Silven', branch = 'ECE');
printDetails(age = 23, 'Silven')

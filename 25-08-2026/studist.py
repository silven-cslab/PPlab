"""
    This python program shows the implementation of the district applications.
"""

districtStudents = {}

while True:
    name = input("Enter your district name: ")

    if name in districtStudents:
        districtStudents[name] += 1

    else:
        districtStudents[name] = 1


    choice = input("Do you want to continue?(Y/n)")

    if choice != 'Y':
        break

print("\n\n")
print(districtStudents)

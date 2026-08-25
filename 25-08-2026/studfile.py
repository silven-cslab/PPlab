"""
    This python program shows the implementation of the dictionaries and files.
"""


file = open("student.txt", "r")

studentDistrict = {}
for district in file:
    district = district.strip("\n")
    if district not in studentDistrict:
        studentDistrict[district] = 0
    else:
        studentDistrict[district] += 1


print(studentDistrict)


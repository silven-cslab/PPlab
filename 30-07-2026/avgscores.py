"""
    * This program takes takes the total no. of student mark entries from the user.
    * Takes all of the values from the user and stores them in a list.
    * And, calcualates the average score.
"""


TotalStds = int(input("Enter the total no. of student marks entries: "))

StdMarks = []

for entry in range(TotalStds):
    marks = int(input(f"Enter the marks of {entry + 1} student: "))
    StdMarks.append(marks)


print(f"The marks of the students are: {StdMarks}")

SumMarks = 0
for mark in StdMarks:
    SumMarks += mark

average = SumMarks // TotalStds

print(f"The average marks of the all students is: {average}")

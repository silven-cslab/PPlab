"""
    This Python Program demonstrates the calculation of average marks of students.
"""

def TakeMarks():
    print("\nEnter the data for all the students: ")

    TotalStudents = 0
    MARKS = []
    while True:
        mark = int(input(f"Student {TotalStudents + 1}: "))
        if mark == 999:
            break
        
        MARKS.append(mark)
        TotalStudents += 1

    ARGS = [tuple(MARKS), TotalStudents]

    return ARGS


def calAverageMarks(MARKS, TotalStudents):
    SumOfMarks = 0


    if MARKS.count(-1) == TotalStudents:
        print("All students are absentees...")
        exit()


    for mark in MARKS:
        if mark != -1:
            SumOfMarks += mark

    Average = SumOfMarks / TotalStudents

    return Average


ARGS = TakeMarks()
print(f"The Average of the marks of students is: {calAverageMarks(ARGS[0], ARGS[1])}")

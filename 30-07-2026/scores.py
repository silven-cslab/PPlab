"""
    This python program finds out the average of the 10 student marks in math subject.
"""

MathMarks = [98, 67, 58, 69, 88, 77, 84, 95, 92, 100]

sumMarks = 0
count = 0

for num in MathMarks:
    sumMarks += num
    count += 1

average = sumMarks // count

print(f"The average of the marks: {MathMarks} is: {average}");

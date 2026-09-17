"""
    This Python Program demonstrates the calculation of average of rainfall readings collected over a month.
"""

def TakeReadings():
    print("\nEnter the readings for the rainfall: ")

    TotalReadings = 0
    READINGS = []
    while True:
        reading = int(input(f"Rainfall Reading {TotalReadings + 1}: "))
        if reading == 999:
            break
        
        READINGS.append(reading)
        if reading != -1:
            TotalReadings += 1

    ARGS = [tuple(READINGS), TotalReadings]

    return ARGS


def calAverageReadings(READINGS, TotalReadings):
    SumOfReadings = 0


    if READINGS.count(-1) == TotalReadings:
        print("All students are absentees...")
        exit()


    for reading in READINGS:
        if reading != -1:
            SumOfReadings += reading

    Average = SumOfReadings / TotalReadings

    return Average


ARGS = TakeReadings()
print(f"The Average of the Rainfall Reading is: {calAverageReadings(ARGS[0], ARGS[1])}")

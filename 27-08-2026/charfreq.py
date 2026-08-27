""" 
    This python program shows the implementation of character frequency calculations in file.
"""


file1 = open("second.txt", "r")
filetext = file1.read()

CHARS = dict()

for line in filetext:
    for word in line:
        for char in word:
            if char in CHARS:
                CHARS[char] += 1
            else:
                CHARS[char] = 1

file1.close()

print("\n  ====== Character Frequency ========")
for char, freq in CHARS.items():
    print(char, freq)

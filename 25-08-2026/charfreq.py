""" 
    This pythomn program shows the implementation of character frequency calculations in file.
"""


file1 = open("wiki.txt", "r")

CHARS = {}

for line in file1:
    for word in line:
        for char in word:
            if char in CHARS:
                CHARS[char] += 1
            else:
                CHARS[char] = 1

print("\n  ====== Character Frequency ========")
for char in CHARS:
    print(char)

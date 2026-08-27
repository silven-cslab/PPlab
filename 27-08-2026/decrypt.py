

SubstitutionTable = {
        "T" : "E",
        "O" : "I",
        "L" : "S",
        "I" : "H",
        "Z" : "T",
        "K" : "R",
        "G" : "O",
        "E" : "C",
        "A" : "K",
        "D" : "M",
        "S" : "L",
        "Q" : "A",
        "V" : "W",
        "N" : "Y",
        "F" : "N", 
        "C" : "V",
        "R" : "D",
        "U" : "G",
        "W" : "B",
        "X" : "U",
        "Y" : "F",
        "H" : "P"
};


opencipher = open("first.txt", "r")
opendecoded = open("firstdecoded.txt", "w")

ciphertext = opencipher.read()

for line in ciphertext:
    for word in line:
        for char in word:
            if char in SubstitutionTable:
                print(SubstitutionTable[char], end = '')
                opendecoded.write(SubstitutionTable[char])
            else:
                print(char, end = '')
                opendecoded.write(char)


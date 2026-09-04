
SubstitutionTable = {
    "S" : "T",
    "B" : "O",
    "D" : "A",
    "P" : "J",
    "U" : "E",
    "J" : "N", 
    "Y" : "R",
    "Q" : "C",  
    "X" : "D",
    "W" : "V",
    "L" : "P",  
    "V" : "L",
    "K" : "B",
    "C" : "W",
    "T" : "S",
    "N" : "I",
    "R" : "H",  
    "H" : "G",  
    "F" : "U",  
    "Z" : "F",
    "I" : "Y",
    "A" : "M",
    "O" : "K"
}

opencipher = open("second.txt", "r")
ciphertext = opencipher.read()


for line in ciphertext:
    for word in line:
        for char in word:
            if char in SubstitutionTable:
                print(SubstitutionTable[char], end = '')
            else:
                print(char, end = '')


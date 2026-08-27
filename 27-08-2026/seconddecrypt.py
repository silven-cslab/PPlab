
SubstitutionTable = {
    "D" : "A",
    "J" : "T",
    "N" : "E",
    "K" : "N"
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


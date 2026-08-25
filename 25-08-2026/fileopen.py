File = open("example.txt", "r")

#print(File.read())

#for line in File:
#    print(line.strip("\n"))

FileW = open("f2.txt", "w")

for line in File:
    FileW.write(line)

import fileinput
import sys

hexCount = {}
intToHex = {}
count = 1

for line in fileinput.input():
    line = line.strip('\n')
    line = line.lstrip('0')

#  converts hex to int and pairs with corresponding value

    intToHex[int(line, 16)] = line
    if line not in hexCount:
        hexCount[line] = 1
    else:
        hexCount[line] = hexCount[line] + 1

intValues = list(intToHex)
intValues.sort()

for intValue in intValues:
    hexNumber = intToHex[intValue]
    if hexCount[hexNumber] > 1:
        print(hexNumber, hexCount[hexNumber])

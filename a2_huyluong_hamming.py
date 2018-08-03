import sys

# convert system arguments into base 16 hexadecimals
input1 = int(sys.argv[1], 16)
input2 = int(sys.argv[2], 16)

def hammingdistance(s1, s2):
    # convert int sys.argv to hex
    if len(hex(s1)) != len(hex(s2)):
        print ("Values are not the same length")
    else:
        # convert to binary string, XOR the 2 hex values and count 1's to determine hamming distance
        distance = bin(s1 ^ s2).count('1')
        print (distance)

hammingdistance(input1, input2)

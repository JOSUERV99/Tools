from math import log, ceil

#Converting any number of any base to another base

def binToDec(binario):
    decNumber = 0
    binario=binario[::-1]
    for i in range(0, len(binario)):
        decNumber += int(binario[i])* 2**i
    return decNumber

def decToBin(decimal):

    def calculateSpaces(decimal, counter):
        if decimal > 2**counter:
            return calculateSpaces(decimal-2**counter, counter+1)
        else:
            return counter

    def bin(dec, spaces):
        if spaces < 0:
            return ""

        if 2**spaces <= dec:
            return "1" + bin(dec-2**spaces, spaces-1)
        elif 2**spaces > dec:
            return "0" + bin(dec, spaces-1)
    
    spaces = calculateSpaces(decimal, 0)
    if decimal == 0:
        return "0"
    else:
        return bin(decimal, spaces)

def decToHex(decimal):
    hexa = ""
    binario = decToBin(decimal)[::-1]
    while (len(binario)%4 != 0):
        binario+="0"
    currentDigit = 0
    print(binario, end="\t")
    #binario = binario[::-1]
    counter = 0
    for i in range(int(len(binario)/4)):
        for j in range(4):    
            currentDigit += int(binario[counter]) * 2**(j)
            counter+=1
        if currentDigit < 10:
            hexa += str(currentDigit)
        else:
            hexa += str(chr(currentDigit+87)).upper()
        currentDigit = 0
    return hexa[::-1]

print("--HEX--")
numeros = [0, 15, 16, 1231, 11, 12]
for i in numeros:
    print(i, "->", decToHex(i))

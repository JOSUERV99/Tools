"""
    Converting any number of any base to another base with a tkinter gui
    @author: Josue Rojas
    @since: 03/01/2020

        BIN -> HEX *
        BIN -> OCT
        BIN -> DEC *
        HEX -> BIN
        HEX -> OCT
        HEX -> DEC
        OCT -> BIN
        OCT -> HEX
        OCT -> DEC
        DEC -> BIN *
        DEC -> HEX *
        DEC -> OCT
"""

from math import log, ceil
import tkinter
headers = ["BIN", "HEX", "OCT", "DEC"]

def binToOct(binario):
    octal = ""
    for i in range(len(binario)):
        if binario[i] == 1:
            octal += str( 8**i )
    return octal[::-1]

def binToHex(binario):
    return decToHex(binToDec(binario))

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
        return "0000"
    else:
        binario = bin(decimal, spaces)[::-1]
        while(len(binario)%4!=0):
            binario+="0"
        return binario[::-1]

def decToHex(decimal):
    hexa = ""
    binario = decToBin(decimal)[::-1]
    currentDigit = 0
    #print(binario, end="\t")
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

numeros = [0, 15, 16, 1231, 31, 1, 3]
bina = ["1101", "01010001", "10100001", "11110001", "10110111", "00000001", "11110001"]
for i in range(len(numeros)):
    print("DEC->BIN", numeros[i], "= "+decToBin(numeros[i]))
    print("BIN->HEX", bina[i], "= "+binToHex(bina[i]))
    print("DEC->HEX", numeros[i], "= "+decToHex(binToDec(decToBin(numeros[i]))))
    print("BIN->DEC", bina[i], "= "+str(binToDec(bina[i])))
    print("     BIN->OCT", bina[i], "= "+binToOct(bina[i]))

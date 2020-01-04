"""
    Converting any number of any base to another base with a tkinter gui
    @author: Josue Rojas
    @since: 03/01/2020

        BIN -> HEX *
        BIN -> OCT
        BIN -> DEC *
        HEX -> BIN
        HEX -> OCT
        HEX -> DEC x
        OCT -> BIN
        OCT -> HEX
        OCT -> DEC *
        DEC -> BIN *
        DEC -> HEX *
        DEC -> OCT
"""

from math import log, ceil
import tkinter
validChars = "0123456789ABCDEF" #TODO: modifiy allToDec for hex numbers
headers = ["BIN", "HEX", "OCT", "DEC"]

def allToDec(number, base=10):
    decimal = 0
    number = number[::-1]
    for i in range(len(number)):
        decimal += int(number[i]) * base**i
    return decimal

def binToOct(binario):
    octal = ""
    for i in range(len(binario)):
        if binario[i] == 1:
            octal += str( 8**i )
    return octal[::-1]

def binToHex(binario):
    return decToHex(allToDec(binario, base=2))

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
    print("DEC->HEX", numeros[i], "= "+decToHex(allToDec(decToBin(numeros[i]), base=2)))
    print("BIN->DEC", bina[i], "= "+str(allToDec(bina[i], base=2)))
    print("     BIN->OCT", bina[i], "= "+binToOct(bina[i]))

decTest =  ["1010", 2, "F"]
print("123", allToDec("123", 8))


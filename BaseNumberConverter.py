from math import log, ceil

#Converting any number of any base to another base

def binToDec(binario):
    decNumber = 0
    binario=binario[::-1]
    for i in range(0, len(binario)):
        decNumber += int(binario[i])* 2**i
    return decNumber

def decToBin(decimal):
    binario = "" # TODO: conversion de numeros negativos, and bug
    if decimal != 0:        
        for i in range(ceil(log(decimal))+1, 0, -1):
            print(decimal, end="\t")
            if 2**i <= decimal:
                binario += "1"
                decimal -= 2**i
            else:
                binario += "0"
    else:
        return "0"
    return binario

def decToHex(decimal):
    hexa = "" # TODO: all xD
    binario = decToBin(decimal)[::-1]
    print(binario)
    aux = bandera = 0
    for i in range(len(binario), 4):
        print(aux)
        aux = 0


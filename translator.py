#!/usr/bin/env python2

import sys
myFile = open("test","r")
myFile2 = open("output.txt","w")
line = myFile.readline()
nl = ''

freqDict = {"a" : " ", "b" : " ", "c" :" ", "d" :" ", "e" :" ", "f" :" ", "g" :" ", "h" :" ", "i" :" ", "j" :" ", "k" :" ", "l" :" ", "m" :" ", "n" :" ", "o" :" ", "p" :" ", "q" :" ", "r" :" ", "s" :" ", "t" :" ", "u" :" ", "v" :" ", "w" :" ", "x" :" ", "y" :" ", "z" : " ", "A" : " ", "B" : "e", "C" :" ", "D" :" ", "E" :" ", "F" :" ", "G" :" ", "H" :" ", "I" :" ", "J" :" ", "K" :" ", "L" :" ", "M" :" ", "N" :" ", "O" :" ", "P" :" ", "Q" :"t", "R" :" ", "S" :" ", "T" :" ", "U" :" ", "V" :" ", "W" :" ", "X" :" ", "Y" :" ", "Z" : "a"}

while line:
    for letter in line:
        if letter in freqDict:
            nl +=freqDict[letter]
    myFile2.write(nl)
    line = myFile.readline()
myFile.close()

#!/usr/bin/env python2
#fills a sqlite3 database with data from a plaintext file

import sys
myFile = open("test2","r")
line = myFile.readline()
myDict = {}
myDict2 = {}
totalLength = 0

freqDict = {"a" : 8.167, "b" : 1.49, "c" : 2.78, "d" : 4.253, "e" : 12.702, "f" : 2.228, "g" : 2.015, "h" : 6.094, "i" : 6.966, "j" : 0.153, "k" : 0.772, "l" : 4.025, "m" : 2.406, "n" : 6.749, "o" : 7.507, "p" : 1.929, "q" : 0.095, "r" : 5.987, "s" : 6.327, "t" : 9.056, "u" : 2.758, "v" : 0.978, "w" : 2.360, "x" : 0.150, "y" : 1.974, "z" : 0.07}


while line:
    for letter in line:
        if letter in myDict:
            myDict[letter] += 1
        else:
            myDict[letter] = 1
    totalLength += len(line)
    line = myFile.readline()
myFile.close()

print
print "TOTAL FREQUENCIES PER LETTER IN CIPHERTEXT:"
print
for letter in myDict:
    print (letter,':',str(myDict[letter]))  
print
print "FREQUENCIES IN CIPHERTEXT IN ALPHABETICAL ORDER WITH PERCENTAGES"
print
for letter in myDict:
    myDict2[letter] = float(float(myDict[letter]) / float(totalLength)) * 100
    print (letter,':',str(myDict2[letter]))


reverseFreqDict = {}
listFreq = []
print
print "FREQUENCES IN THE ENGLISH LANGUAGE IN ALPHABETICAL ORDER WITH PERCENTAGES"
print
for letter in freqDict:
    print (letter, ":",str(freqDict[letter]))
    reverseFreqDict[freqDict[letter]] = letter
    listFreq.append(freqDict[letter])
print
print "LETTERS IN THE ENGLISH LANGUAGE IN ORDER OF FREQUENCY:"
print

listFreq = sorted(listFreq,reverse=True)
for number in listFreq:
    print(reverseFreqDict[number], ":", str(number))

print
print "LETTERS IN CIPHERTEXT IN ORDER OF FREQUENCY"
print 

reverseFreqDict = {}
listFreq = []
for letter in myDict2:
    if myDict2[letter] not in reverseFreqDict:
        reverseFreqDict[myDict2[letter]] = letter
    else:
        reverseFreqDict[myDict2[letter]] = reverseFreqDict[myDict2[letter]] + "," + letter 
    listFreq.append(myDict2[letter])
listFreq = sorted(listFreq,reverse=True)

for number in listFreq:
    print(reverseFreqDict[number], ":", str(number))

#!/bin/usr/python3
#aoe2023 activity 1

f = open("input.txt", "r")

import sys
from time import sleep

DEBUG = False

numbers = []

digits = {
    "one" : "1",
    "two" : "2",
    "three": "3",
    "four" : "4",
    "five": "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
    }

line_counter = 1

for line in f.readlines():
    ## DEBUG
    if DEBUG:
        print("*********")
        print("***LINE*** ", line_counter, " | ", line.strip("\n"))
        line_counter += 1
        print("*********")
        sleep(0.5)
        
    # find the first digit / number value
    #  keep it's index for later...
    i = 0
    length = len(line)

    n1 = "0"
    n1_i = length
    n2 = "0"
    n2_i = 0

    # check for digits from the start
    while (i < length):
        char = line[i]
        if char.isnumeric():
            n1 = char
            n1_i = i
            break
        i += 1
        
    # check for digits from the end
    i = length - 1
    while (i > -1):
        char = line[i]
        if char.isnumeric():
            n2 = char
            n2_i = i
            break
        i = i - 1

    if DEBUG: print("Digits: ", n1, n2)
    
    # check for words from the start
    for word in digits.keys():

        if DEBUG: print("Word: ", word)
        #if DEBUG: sleep(0.2)

        index = line.find(word)

        # none found...
        if index == -1:
            continue

        # we need to check for duplicates
        dups = line.split(word)
        if DEBUG: print(dups)

        # check from start
        if len(dups[0]) < n1_i:
            n1 = digits[word]
            n1_i = len(dups[0])
            if DEBUG: print("found beginning: ", n1, n1_i)

        # check from the end
        if (length - len(dups[-1])) > n2_i:
            n2 = digits[word]
            n2_i = (length - len(dups[-1])) + (len(word)-1)
            if DEBUG: print("found end: ", n2, n2_i)

            
    
    #sys.exit(0)
    if DEBUG: print("Digits: ", n1, n2, " (after)")
    numbers.append(int(n1 + n2))

# add up all codes
answer = 0
for n in numbers:
    answer += int(n)

print("Answer: ", answer)

### print codes
output = ""
first = True
for n in numbers:
    if first:
        first = False
    else:
        output += ", "
    output += str(n)
    
print(output)

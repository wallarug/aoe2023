#!/bin/usr/python3
#aoe2023 activity 1

f = open("input.txt", "r")

import sys

numbers = []
for line in f.readlines():
    # need to find first number
    for char in line:
        if char.isnumeric():
            n1 = char
            #print(n1)
            break
    # find second number
    i = len(line) - 1
    while (i > -1):
        #print(char)
        char = line[i]
        if char.isnumeric():
            n2 = char
            #print(n2)
            break
        i = i - 1
    #sys.exit(0)
    numbers.append(int(n1 + n2))

# add up all codes
answer = 0
for n in numbers:
    answer += int(n)

print("Answer: ", answer)

### print codes
##output = ""
##first = True
##for n in numbers:
##    if first:
##        first = False
##    else:
##        output += ", "
##    output += str(n)
##    
##print(output)

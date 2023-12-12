#!/bin/usr/python3
# Day 9: Advent of Code

# Higher than: 
# Less than: 
# wrong: 
# correct: 

from sys import exit
DEBUG = False

import os
import math

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)
f = open("input.txt", "r")

def differences(list):
    diff = []
    for i in range(0, len(list) - 1):
        diff.append(list[i + 1] - list[i])
    return diff


answer = 0
values = []
temp_diffs = []
temp_i = 0
all_zero = False

for line in f.readlines():
    # parse line
    line = line.strip().split(" ")
    line = [int(i) for i in line]

    # reset variables
    temp_diffs = []
    temp_i = 0
    all_zero = False

    # add line to temp_diffs
    temp_diffs.append(line)    

    # find differences
    while(all_zero == False):
        temp_diffs.append(differences(temp_diffs[temp_i]))
        temp_i += 1

        #print("Temp diffs (uno): ", temp_diffs)

        for i in range(0, len(temp_diffs[temp_i])):
            if temp_diffs[temp_i][i] == 0:
                all_zero = True
            else:
                all_zero = False
                break

    #print("Differences: ", temp_diffs)
    
    # calculate next value
    prev = 0
    for i in range(len(temp_diffs)-1, 0, -1):
        left = temp_diffs[i-1][-1]
        right = left + prev
        prev = right
        #print("Left: ", left, "Right: ", right, "Prev: ", prev)

    #print("Next value: ", prev)
    values.append(prev)


# sum all values
for i in range(0, len(values)):
    answer += values[i]

f.close()

print("Answer: ", answer)
exit()

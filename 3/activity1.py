#!/bin/usr/python3
# Day 3: Advent of Code

# Higher than: 450182
# Less than: 541680
# wrong: 540998
# correct: 539713

from sys import exit
DEBUG = False

f = open("input.txt", "r")

skip = ["."]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

schematic = f.readlines()

sum = 0

row = 0
column = 0


def check_symbols(data, row, column, length):
    # go along the line until we get to the end (+/- 1 for diagonal)
    start = column - 1
    end = column + length + 1 # (inclusive)

    safety_column = len(data[row]) - 1
    if end > safety_column:
        end = safety_column

    if start < 0:
        start = 0

    if DEBUG:
        print("Checking symbols from " + str(start) + " to " + str(end) + " on line " + str(data[row][start:end]))

    # start with previous line
    if row > 0:
        for i in range(start, end):
            sym = data[row - 1][i]
            if sym in digits:
                continue
            elif sym in skip:
                continue
            else:
                if DEBUG: print("Found symbol: " + sym + " at [" + str(row - 1) + ", " + str(i) + "]")
                return True
    
    # check current line
    for i in range(start, end):
        sym = data[row][i]
        if sym in digits:
            continue
        elif sym in skip:
            continue
        else:
            if DEBUG: print("Found symbol: " + sym + " at [" + str(row) + ", " + str(i) + "]")
            return True
    
    # check next line
    if row < len(data) - 1:
        for i in range(start, end):
            sym = data[row + 1][i]
            if sym in digits:
                continue
            elif sym in skip:
                continue
            else:
                if DEBUG: print("Found symbol: " + sym + " at [" + str(row + 1) + ", " + str(i) + "]")
                return True

    # we didn't find any, return False
    if DEBUG: print("No symbols found")
    return False

## Schematic Structure
#  [line][character]

searching = False
num_col = 0

for line in schematic:
    # we need to check for numbers on the current line,
    #  then do a search to the left, right, top, bottom for values
    column = 0
    for character in line:
        if character in digits:
            # find the end of the number
            if searching == False:
                searching = True
                num_col = column
        else:
            if searching:
                # we found the end of the number
                searching = False
                if DEBUG: print("Found number: " + line[num_col:column])
                # check if the number is higher than the surrounding numbers
                if check_symbols(schematic, row, num_col, column - num_col):
                    if DEBUG: print("Found Symbol!")
                    sum += int(line[num_col:column])

        # increment column
        column += 1
    # increment row
    row += 1

    #if row == 4 and DEBUG:
    #    exit()

# output result
print("Sum: " + str(sum))


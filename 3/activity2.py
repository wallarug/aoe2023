#!/bin/usr/python3
# Day 3: Advent of Code (Activity 2)

# Higher than: 
# Less than: 
# wrong: 
# correct: 84159075

from sys import exit
DEBUG = True

f = open("input.txt", "r")

skip = ["."]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

schematic = f.readlines()

sum = 0
gears = {}

# Gears structure
# ["row, column"] = [values]

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

    value = int(data[row][column:(column+length)])

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
                if sym == "*":
                    if DEBUG: print("Found gear: " + sym + " at [" + str(row - 1) + ", " + str(i) + "]")
                    key = "{0}, {1}".format(row - 1, i)

                    if key not in gears:
                        gears[key] = [value]
                    else:
                        gears[key].append(value)
                    
                    continue
    
    # check current line
    for i in range(start, end):
        sym = data[row][i]
        if sym in digits:
            continue
        elif sym in skip:
            continue
        else:
            if sym == "*":
                    if DEBUG: print("Found gear: " + sym + " at [" + str(row) + ", " + str(i) + "]")
                    key = "{0}, {1}".format(row, i)

                    if key not in gears:
                        gears[key] = [value]
                    else:
                        gears[key].append(value)
                    
                    continue
    
    # check next line
    if row < len(data) - 1:
        for i in range(start, end):
            sym = data[row + 1][i]
            if sym in digits:
                continue
            elif sym in skip:
                continue
            else:
                if sym == "*":
                    if DEBUG: print("Found gear: " + sym + " at [" + str(row + 1) + ", " + str(i) + "]")
                    key = "{0}, {1}".format(row + 1, i)

                    if key not in gears:
                        gears[key] = [value]
                    else:
                        gears[key].append(value)
                    
                    continue

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
                check_symbols(schematic, row, num_col, column - num_col)
                
        # increment column
        column += 1
    # increment row
    row += 1

    #if row == 4 and DEBUG:
    #    exit()

# compile result by multiplying all values in gears
print("compliling result")
for key in gears:
    if DEBUG: print("Key: " + key)
    if DEBUG: print("Values: " + str(gears[key]))
    product = 1
    if len(gears[key]) < 2:
        continue

    for value in gears[key]:
        product *= value
    
    sum += product


# output result
print("Sum: " + str(sum))


#!/bin/usr/python3
# Day 3: Advent of Code

# Higher than: 

from sys import exit


f = open("input.txt", "r")

skip = ["."]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

schematic = f.readlines()
index = 0

for line in schematic:
    # we need to check for numbers on the current line,
    #  then do a search to the left, right, top, bottom for values
    

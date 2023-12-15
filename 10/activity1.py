#!/bin/usr/python3
# Day 10: Advent of Code

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
f = open("test.txt", "r")

answer = 0
grid = []

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print()

class Square:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.distance = 0
        
        if symbol == "S": self.is_start = True
        else: self.is_start = False

        self.travel = []
        self.set_travel()

        self.row = x
        self.column = y

    def set_travel(self):
        if self.symbol == "|":
            self.travel = ["U", "D"]
        elif self.symbol == "-":
            self.travel = ["L", "R"]
        elif self.symbol == "L":
            self.travel = ["U", "R"]
        elif self.symbol == "J":
            self.travel = ["U", "L"]
        elif self.symbol == "7":
            self.travel = ["D", "L"]
        elif self.symbol == "F":
            self.travel = ["D", "R"]
        else: # . and S
            self.travel = []

    def set_distance(self, distance):
        self.distance = distance

    def __str__(self):
        return self.symbol
    
    def __repr__(self):
        return self.symbol




## Read input
x = 0
start_coords = []
for line in f.readlines():
    grid.append([Square(char, x, y) for y, char in enumerate(line.strip())])
    
    y = 0
    for grid_row in grid[x]:
        if grid_row.is_start:
            start_coords = [x, y]
        y += 1
    
    x += 1

## Work out distances...
def get_next_square(square, direction):
    if direction == "U":
        return grid[square.row - 1][square.column]
    elif direction == "D":
        return grid[square.row + 1][square.column]
    elif direction == "L":
        return grid[square.row][square.column - 1]
    elif direction == "R":
        return grid[square.row][square.column + 1]

## We want to go to the first square, which is at S.
current_square = grid[start_coords[0]][start_coords[1]]

## Determine start shape/directions (check everything)
up = get_next_square(current_square, "U")
down = get_next_square(current_square, "D")
left = get_next_square(current_square, "L")
right = get_next_square(current_square, "R")

if "D" in up.travel:
    # valid
    pass
elif "U" in down.travel:
    # valid
    pass
elif "R" in left.travel:
    # valid
    pass
elif "L" in right.travel:
    # valid
    pass

# now we have dealt with the "S" square, we can start with general distance calculation algorithm
# we need to keep track of the distance from the start square
distance = 0



print("Grid: \n")
print_grid(grid)
print("Start coords: ", start_coords)

f.close()

print("Answer: ", answer)
exit()

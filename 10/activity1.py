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

def print_grid_distance(grid):
    for row in grid:
        for col in row:
            distance = col.distance
            if col.symbol == ".": 
                distance = "."
            print(distance, end="")
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

        self.parent = None
        self.visited = False

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
        if self.symbol == "S":
            self.distance = 0
        if self.distance == 0 and self.symbol != ".":
            self.distance = distance
        elif self.symbol == ".":
            self.distance = 0
        else:
            print("Error: distance already set for square ", self.symbol)
            exit()

    def set_parent(self, parent):
        if self.parent == None:
            self.parent = parent

    def set_visited(self):
        self.visited = True
    
    def visited(self):
        return self.visited

    def get_distance(self):
        return self.distance
    
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
    if direction == "U" and square.row - 1 > -1:
        return grid[square.row - 1][square.column]
    elif direction == "D" and (square.row + 1) < len(grid):
        return grid[square.row + 1][square.column]
    elif direction == "L" and square.column - 1 > -1:
        return grid[square.row][square.column - 1]
    elif direction == "R" and (square.column + 1) < len(grid[square.row]):
        return grid[square.row][square.column + 1]
    else:
        return None

## Data structure
stack = []

## We want to go to the first square, which is at S.
current_square = grid[start_coords[0]][start_coords[1]]
stack.append(current_square)

# now we have dealt with the "S" square, we can start with general distance calculation algorithm
# we need to keep track of the distance from the start square
distance = 0

print_grid(grid)

while (len(stack) > 0):
    # get the next square
    current_square = stack.pop(0)

    print("Current square: ", current_square.symbol, " at ", current_square.row, ", ", current_square.column)

    # check if it's a dot
    if current_square.symbol == ".":
        # if it is, skip it
        continue
    
    # if it's not, set the distance
    if current_square.symbol != "S": current_square.set_distance(current_square.parent.distance + 1)
    
    # increment the distance
    # distance += 1
    
    # get the next square
    up = get_next_square(current_square, "U")
    down = get_next_square(current_square, "D")
    left = get_next_square(current_square, "L")
    right = get_next_square(current_square, "R")

    # add the next squares to the stack
    if up and "D" in up.travel:
        if up.visited == False:
            up.set_visited()
            up.set_parent(current_square)
            print("went up")
            stack.append(up)
    if down and "U" in down.travel:
        if down.visited == False:
            down.set_visited()
            down.set_parent(current_square)
            print("went down")
            stack.append(down)
    if left and "R" in left.travel:
        if left.visited == False:
            left.set_visited()
            left.set_parent(current_square)
            print("went left")
            stack.append(left)
    if right and "L" in right.travel:
        if right.visited == False:
            right.set_visited()
            right.set_parent(current_square)
            print("went right")
            stack.append(right)

    print(stack)

    if current_square.distance > distance:
        distance = current_square.distance


print("Grid: \n")
print_grid(grid)
print("Distances: \n")
print_grid_distance(grid)

print("Start coords: ", start_coords)

## find the furthest distance.

f.close()

print("Answer: ", distance)
exit()

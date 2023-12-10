#!/bin/usr/python3
# Day 8: Advent of Code

# Higher than: 
# Less than: 
# wrong: 
# correct: 

from sys import exit
DEBUG = False

import os

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)


class MapElement:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def go(self, direction):
        if direction == "L":
            return self.left
        elif direction == "R":
            return self.right
        else:
            print("ERROR: Invalid direction: ", direction)
            exit()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class DirectionStack:
    def __init__(self):
        self.stack = []
        self.index = -1

    def add(self, direction):
        self.stack.append(direction)
    
    def next(self):
        self.index += 1
        if self.index == len(self.stack): self.index = 0
        return self.stack[self.index]

    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return str(self.stack)

answer = 0


f = open("input.txt", "r")

directions = DirectionStack()
map = {}

blah = True

for line in f.readlines():
    if blah:
        for char in line.strip():
            directions.add(char)
        blah = False
        continue
    
    if line == "\n":
        continue
    
    else:
        # grab the directions...
        line = line.strip().split("=")

        name = line[0].strip()
        left = line[1].strip().split(", ")[0][1:]
        right = line[1].strip().split(", ")[1][:-1]

        map[name] = MapElement(name, left, right)

# we should have everything now.

# Let's follow the map and see if we can reach "ZZZ"
target = "ZZZ"
steps = 0
next = "AAA"

while(next != target):
    d = directions.next()
    #print("Going ", d, " at ", next)
    next = map[next].go(d)
    #print("Got to : ", next)
    steps += 1

# close the file
f.close()


print("Answer: ", steps)
exit()



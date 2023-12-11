#!/bin/usr/python3
# Day 8: Advent of Code (Part 2)

# Higher than: 
# Less than:  33414692793508173913740
# wrong: 
# correct: 22289513667691

from sys import exit
DEBUG = False

import os
import math

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)


class MapElement:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

        self.start_node = False
        self.end_node = False

    def set_start_node(self):
        if self.name[2] == "A":
            self.start_node = True
            return True
        return False
    
    def set_end_node(self):
        if self.name[2] == "Z":
            self.end_node = True
            return True
        return False

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

next_nodes = []

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

        map[name].set_end_node()

        if map[name].set_start_node():
            next_nodes.append(name)
        


# we should have everything now.

# Let's follow the map and see if we can reach "ZZZ"
steps = 0
all_z = False
results = []
i = 0

while(len(next_nodes) > 0):
    d = directions.next()
    all_z = True

    l = len(next_nodes)
    i = 0
    while(i < l):
        next_nodes[i] = map[next_nodes[i]].go(d)
        if next_nodes[i][2] == "Z":
            results.append(steps+1)
            next_nodes.remove(next_nodes[i])
            l = l - 1
            print("FOUND A Z!!")
            print("Next Nodes: ", next_nodes)
            #exit()
            continue
        i += 1

    steps += 1

    if steps % 10000 == 0:
        print("Steps: ", steps)
        print("Next Nodes: ", next_nodes)

# close the file
f.close()

# Use LCM to find the answer
def lcm(list):
    lcm = 1
    for i in list:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm

answer = lcm(results)

print("Results: ", results)

print("Answer: ", answer)
exit()



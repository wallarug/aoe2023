#!/bin/usr/python3
# Day 6: Advent of Code (Part 2)

# Higher than: 
# Less than: 
# wrong: 
# correct: 28545089

from sys import exit
DEBUG = False

import os

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

answer = 1

f = open("input.txt", "r")

data = f.readlines()

# line one is Time.
times = data[0].split(":")[1].strip().split("  ")

for x in times:
    if x == '':
        times.remove(x)

times = [int(x) for x in times]

# join the values in times together to form a single int
times = int("".join(str(x) for x in times))

distances = data[1].split(":")[1].strip().split("  ")
for x in distances:
    if x == "":
        distances.remove(x)
distances = [int(x) for x in distances]

# join the values in distances together to form a single int
distances = int("".join(str(x) for x in distances))

print("Times: ", times)
print("Distances: ", distances)

beets = []
battle_star_galactica = 0
# brute force method: check every single speed to see if distance can be beaten.
battle_star_galactica = 0
for t in range(0, times):
    # hold the button for t time, check if distance is beaten.
    distance = t * (times - t)
    if distance > distances:
        battle_star_galactica += 1
    #print("[", x, "] Time: ", t, " Distance: ", distance, " Beets: ", battle_star_galactica, " Win Distance: ", distances[x])

#print("Beets: ", beets)

# for beet in beets:
#     answer *= beet

# close the file
f.close()


print("Answer: ", battle_star_galactica)
exit()



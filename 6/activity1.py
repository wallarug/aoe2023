#!/bin/usr/python3
# Day 6: Advent of Code

# Higher than: 
# Less than: 
# wrong: 
# correct: 6209190

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

distances = data[1].split(":")[1].strip().split("  ")
for x in distances:
    if x == "":
        distances.remove(x)
distances = [int(x) for x in distances]

print("Times: ", times)
print("Distances: ", distances)

beets = []
battle_star_galactica = 0
# brute force method: check every single speed to see if distance can be beaten.
for x in range(len(times)):
    battle_star_galactica = 0
    for t in range(0, times[x]):
        # hold the button for t time, check if distance is beaten.
        distance = t * (times[x] - t)
        if distance > distances[x]:
            battle_star_galactica += 1
        #print("[", x, "] Time: ", t, " Distance: ", distance, " Beets: ", battle_star_galactica, " Win Distance: ", distances[x])
    beets.append(battle_star_galactica)

print("Beets: ", beets)

for beet in beets:
    answer *= beet

# close the file
f.close()


print("Answer: ", answer)
exit()



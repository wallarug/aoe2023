#!/bin/usr/python3
# Day 4: Advent of Code, Activity 2

# Higher than: 5756587
# Less than: 
# wrong: 
# correct: 6874754

from sys import exit
DEBUG = False

import os

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

f = open("input.txt", "r")

# format: Card 1: winning number list | my numbers list

# variables
sum = 0
wins = {}
temp_sum = 0

for line in f.readlines():
    temp_sum = 0
    data = line.strip("\n").split(":")
    card = int(data[0].strip(" ").split(" ")[-1])
    data = data[1].split("|")  # discard the card number
    winning_numbers = data[0].strip(" ").split(" ")

    # check for empty strings
    for x in winning_numbers:
        if x == '':
            winning_numbers.remove(x)

    winning_numbers = [int(x.strip(" ")) for x in winning_numbers]
    my_numbers = data[1].strip(" ").split(" ")

    # check for empty strings
    for x in my_numbers:
        if x == '':
            my_numbers.remove(x)

    my_numbers = [int(x.strip(" ")) for x in my_numbers]

    # calculate score
    for x in my_numbers:
        if x in winning_numbers:
            temp_sum += 1
    
    # add wins to array
    wins[card] = temp_sum


copies = {}

for w in wins:
    # count self...
    if w not in copies:
        copies[w] = 1
    else:
        copies[w] += 1

    # zeros do not make copies
    if wins[w] == 0:
        continue

    # check for overflow
    end = w+wins[w]+1
    if end > len(wins)+1:
        end = len(wins)+1
    
    # add cards to copies
    for x in range(w+1, end):
        if x in copies:
            copies[x] += copies[w]
        else:
            copies[x] = copies[w]

print(copies)
print("wins: ")
print(wins)

# sum up the number of cards
for x in copies:
    sum += copies[x]

f.close()

print("Sum is: ", sum)
exit()



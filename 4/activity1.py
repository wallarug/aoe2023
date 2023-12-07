#!/bin/usr/python3
# Day 4: Advent of Code

# Higher than: 
# Less than: 42150
# wrong: 
# correct: 21088

from sys import exit
DEBUG = False

import os

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

f = open("input.txt", "r")

# format: Card 1: winning number list | my numbers list

# variables
sum = 0
temp_sum = 0

for line in f.readlines():
    temp_sum = 0
    data = line.strip("\n").split(":")
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
    
    if temp_sum > 1:
        sum += 2**(temp_sum-1)
    elif temp_sum == 1:
        sum += 1
    ## 1 = 1 (calculate 2**1 = 2)
    ## 2 = 4 (calculate 2**2 = 4)
    ## 3 = 8 (calculate 2**3 = 8)


f.close()

print("Sum is: ", sum)
exit()



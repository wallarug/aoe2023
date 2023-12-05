#!/bin/usr/python3
# Day 2: Advent of Code

# Higher than: 361

from sys import exit

## Totals Allowed
total_red = 12
total_green = 13
total_blue = 14

## Game List
games = []

class Game:
    def __init__(self, identifier):
        self.gid = int(identifier)

        self.total_red = 0
        self.total_green = 0
        self.total_blue = 0

        self.games = {}

        self.power = 0

        self.valid = None

    def hand(self, line):
        # split by subsets
        subsets = line.split(";")

        # temporary counts
        red = 0
        blue = 0
        green = 0

        sub_id = 1

        for subset in subsets:
            # create a dictionary to hold results for later
            self.games[sub_id] = {}

            # split the individual hand...
            cubes = subset.split(",")
            
            for cube in cubes:
                value = self.parse_number(cube)
                
                if "red" in cube:
                    self.games[sub_id]["red"] = value
                    red += value
                elif "green" in cube:
                    self.games[sub_id]["green"] = value
                    green += value
                elif "blue" in cube:
                    self.games[sub_id]["blue"] = value
                    blue += value
            
            sub_id += 1

        self.total_red = red
        self.total_green = green
        self.total_blue = blue

    def parse_number(self, term):
        term = term.strip(" ")
        parts = term.split(" ")
        return int(parts[0])

    def pow_minimum_cubes(self):
        r = 0
        b = 0
        g = 0

        for i in self.games:
            for key in self.games[i].keys():
                if key is "red":
                    if self.games[i]["red"] > r:
                        r = self.games[i]["red"]
                if key is "green":
                    if self.games[i]["green"] > g:
                        g = self.games[i]["green"]
                if key is "blue":
                    if self.games[i]["blue"] > b:
                        b = self.games[i]["blue"]

        self.power = r * g * b        

    def is_valid_per_hand(self, r, g, b):
        for i in self.games:
            for key in self.games[i].keys():
                if key is "red":
                    if self.games[i]["red"] > r:
                        self.valid = False
                        return False
                if key is "green":
                    if self.games[i]["green"] > g:
                        self.valid = False
                        return False
                if key is "blue":
                    if self.games[i]["blue"] > b:
                        self.valid = False
                        return False
        self.valid = True
        return True

    def is_valid_per_game(self, r, g, b):
        if (self.total_red <= r) and (self.total_green <= g) \
            and (self.total_blue <= b):
            self.valid = True
        else:
            self.valid = False

        return self.valid
    
    def is_valid(self, r, g, b):
        # check per hand as default
        return self.is_valid_per_hand(r, g, b)    

    def __str__(self):
        return "id: {0} [{5}], totals: r: {1}, g: {2}, b: {3}.  Array: {4}".format(self.gid,
                                                                             self.total_red,
                                                                             self.total_green,
                                                                             self.total_blue,
                                                                             self.games,
                                                                             self.valid)
    def __repr__(self):
        return "id: {0} [{5}], totals: r: {1}, g: {2}, b: {3}.  Array: {4}".format(self.gid,
                                                                             self.total_red,
                                                                             self.total_green,
                                                                             self.total_blue,
                                                                             self.games,
                                                                             self.valid)


f = open("input.txt", "r")

for line in f.readlines():
    data = line.strip("Game ")
    data = data.split(":")

    g = Game(data[0])
    g.hand(data[1])

    g.is_valid(total_red, total_green, total_blue)
    g.pow_minimum_cubes()

    games.append(g)

    print(g)

sum_valid_ids = 0
sum_powers = 0

for game in games:
    sum_powers += game.power
    
    #if game.is_valid(total_red, total_green, total_blue):
    #    sum_valid_ids += game.gid

print("Sum of powers: ", sum_powers)
      

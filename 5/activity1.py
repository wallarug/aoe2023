#!/bin/usr/python3
# Day 5: Advent of Code

# Higher than: 
# Less than: 
# wrong: 
# correct: 251346198

from sys import exit
DEBUG = False

import os

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

f = open("input.txt", "r")

class SpecialMap:
    def __init__(self, desc):
        self.description = desc

        self.sources = []
        self.destinations = []
        self.ranges = []

    def add_to_map(self, source, destination, range):
        self.sources.append(source)
        self.destinations.append(destination)
        self.ranges.append(range)

    def find_destination(self, search_value):
        # first check the exiting ranges
        for i in range(len(self.sources)):
            start_s = self.sources[i]
            start_d = self.destinations[i]
            r = self.ranges[i]

            # we are searching for a value, we can do a fast search first.  
            # TODO: check inclusive/exclusive
            if (search_value <= start_s + r) and (search_value >= start_s):
                # the value is in this range, return mapped value
                offset = start_d - start_s
                return search_value + offset 
        
        # the value does not confirm to a map, so just return the value (1:1 mapping)
        return search_value
    
    def __str__(self):
        return self.description
    
    def __repr__(self):
        return self.description
        

# variables
seeds = []
maps = {}
maps["seed-to-soil"] = SpecialMap("seed-to-soil")
maps["soil-to-fertilizer"] = SpecialMap("soil-to-fertilizer")
maps["fertilizer-to-water"] = SpecialMap("fertilizer-to-water")
maps["water-to-light"] = SpecialMap("water-to-light")
maps["light-to-temperature"] = SpecialMap("light-to-temperature")
maps["temperature-to-humidity"] = SpecialMap("temperature-to-humidity")
maps["humidity-to-location"] = SpecialMap("humidity-to-location")

# temp variables
current_map = None

# read in data and build the maps
for line in f.readlines():
    # hardcode some of the information
    if line.startswith("seeds"):
        seeds = line.strip("\n").split(":")[1].split(" ")
        print(seeds)

        # remove empty strings
        for x in seeds:
            if x == '':
                seeds.remove(x)

        seeds = [int(x) for x in seeds]
        continue

    # if it is not a seed, it is a map
    if "map" in line:
        data = line.strip("\n").split(":")
        map_name = data[0].strip(" ").split(" ")[0]
        current_map = maps[map_name]
        continue

    if line == "\n":
        continue

    # this is where we input the data...
    data = line.strip("\n").split(" ")
    current_map.add_to_map(int(data[1]), int(data[0]), int(data[2]))
    continue

# Phase 2 - actually working out the seed locations
lowest_location = 999999999999999999999999999999999999
lowest_seed = 0

for seed in seeds:
    # first, we need to find the soil location
    soil_location = maps["seed-to-soil"].find_destination(seed)
    #print("seed: ", seed, "soil location: ", soil_location)

    # next, we need to find the fertilizer location
    fertilizer_location = maps["soil-to-fertilizer"].find_destination(soil_location)
    #print("seed: ", seed, "fertilizer location: ", fertilizer_location)

    # next, we need to find the water location
    water_location = maps["fertilizer-to-water"].find_destination(fertilizer_location)
    #print("seed: ", seed, "water location: ", water_location)

    # next, we need to find the light location
    light_location = maps["water-to-light"].find_destination(water_location)
    #print("seed: ", seed, "light location: ", light_location)

    # next, we need to find the temperature location
    temperature_location = maps["light-to-temperature"].find_destination(light_location)
    #print("seed: ", seed, "temperature location: ", temperature_location)

    # next, we need to find the humidity location
    humidity_location = maps["temperature-to-humidity"].find_destination(temperature_location)
    #print("seed: ", seed, "humidity location: ", humidity_location)

    # finally, we need to find the location
    location = maps["humidity-to-location"].find_destination(humidity_location)
    #print("seed: ", seed, "location: ", location)

    # print the location
    #print("seed: ", seed, "location: ", location)

    # check for lowest location seed
    if location < lowest_location:
        lowest_location = location
        lowest_seed = seed

# close the file
f.close()


print("Lowest Location: ", lowest_location)
exit()



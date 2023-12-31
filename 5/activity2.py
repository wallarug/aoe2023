#!/bin/usr/python3
# Day 5: Advent of Code, Part 2

# Higher than: 
# Less than: 72263011
# wrong: 
# correct: 

from sys import exit
DEBUG = False

import os
from threading import Thread

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

f = open("input.txt", "r")

class SeedPair:
    def __init__(self, start, rg):
        self.start = start
        self.end = start + rg
        self.next = start

    def in_range(self, value):
        if value >= self.start and value <= self.end:
            return True
        else:
            return False
        
    def get_next(self):
        if self.next > self.end:
            return None
        else:
            self.next += 1
            return self.next - 1

    def __str__(self):
        return "start: " + str(self.start) + " end: " + str(self.end)

    def __repr__(self):
        return "start: " + str(self.start) + " end: " + str(self.end)

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
        old_seeds = line.strip("\n").split(":")[1].split(" ")
        #print(old_seeds)

        # remove empty strings
        for x in old_seeds:
            if x == '':
                old_seeds.remove(x)

        old_seeds = [int(x) for x in old_seeds]
        #print(old_seeds)

        ## Seeds are now pairs
        for i in range(0, len(old_seeds), 2):
            seeds.append(SeedPair(old_seeds[i], old_seeds[i+1]))

        #print(seeds)
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

# close the file
f.close()

# Phase 2 - actually working out the seed locations
lowest_location = 999999999999999999999999999999999999
lowest_seed = 0
counter = 0

results = [None] * 10
threads = [None] * 10

def check_seed(seed, maps):
    soil_location = maps["seed-to-soil"].find_destination(seed)
    fertilizer_location = maps["soil-to-fertilizer"].find_destination(soil_location)
    water_location = maps["fertilizer-to-water"].find_destination(fertilizer_location)
    light_location = maps["water-to-light"].find_destination(water_location)
    temperature_location = maps["light-to-temperature"].find_destination(light_location)
    humidity_location = maps["temperature-to-humidity"].find_destination(temperature_location)
    location = maps["humidity-to-location"].find_destination(humidity_location)
    return location

# Multi-threaded version
def compute_seed(tid, seed_pair, maps, results): 
    # using: maps, results, seed_pair
    local_lowest_location = 999999999999999999999999999999999999
    print("Starting thread: ", tid)
    for seed in range(seed_pair.start, seed_pair.end, 1000):
        location = check_seed(seed, maps)

        if location < local_lowest_location:
            local_lowest_location = location
            print("New Lowest: ", local_lowest_location, " from seed: ", seed)
            print("Start fine-grained search")
            lseed = seed
            for k in range(seed - 999, seed):
                l2 = check_seed(k, maps)
                if l2 < local_lowest_location:
                    local_lowest_location = l2
                    print("found new! loc: ", l2, " from seed: ", seed)
            print("End fine-grained search with lowest: ", local_lowest_location)
                
    
    results[tid] = local_lowest_location
    print("Ending thread: ", tid)

# start the threads
counter = 0
for seed_pair in seeds:
    threads[counter] = Thread(target=compute_seed, args=(counter, seed_pair, maps, results))
    if counter == 1: threads[counter].start()
    counter += 1

#for i in range(len(threads)):
#    threads[i].join()

threads[1].join()
print("Result for thread 1: ", results[1])
exit()

# find the lowest location
print(results)
print("Lowest Location: ", min(results))
exit()

for seed_pair in seeds:
    counter += 1
    print("Computing Seed Range ", counter)
    for seed in range(seed_pair.start, seed_pair.end):
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

        # check for lowest location seed
        if location < lowest_location:
            lowest_location = location
            lowest_seed = seed

    
# close the file
f.close()


print("Lowest Location: ", lowest_location)
exit()



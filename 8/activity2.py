#!/bin/usr/python3
# Day 7: Advent of Code (Part 2)

# Higher than: 246724914
# Less than:  247967442, 247941042
# wrong:  
# correct: 247899149

from sys import exit
DEBUG = False

import os

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

card_ranks = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J"
card_ranks = card_ranks.split(", ")

rank_list = [50, 40, 30, 20, 1]

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.rank = 0
        
        self.counts = {}
        self.type = 0

        # run the calculations on creation
        self.count_type()

    def count_type(self):
        for char in self.cards:
            for card in card_ranks:
                if card == char:
                    if card in self.counts:
                        self.counts[card] += 1
                    else:
                        self.counts[card] = 1
        
        #print(self.counts)

        # determine the type of hand
        # Types of Hands in Win Order:
        # Five of a Kind = 50
        # Four of a Kind = 40
        # Full House = 32
        # Three of a Kind = 30
        # Two Pair = 22
        # One Pair = 20
        # High Card = 1
        for key in self.counts:
            if key == "J":      # skip jokers, they mean nothing on their own.
                continue
            if self.counts[key] == 5:
                self.rank = 50              # Five of a Kind
                break
            elif self.counts[key] == 4:
                self.rank = 40              # Four of a Kind
                break
            elif (self.counts[key] == 3 and self.rank == 20) or (self.counts[key] == 2 and self.rank == 30):
                self.rank = 32              # Full House
                break
            elif self.counts[key] == 3:
                self.rank = 30              # Three of a Kind
            elif self.counts[key] == 2 and self.rank == 20:
                self.rank = 22              # Two Pair
            elif self.counts[key] == 2:
                self.rank = 20              # One Pair

        # if no cards match, then we need to set rank to 1
        if self.rank == 0:
            self.rank = 1                   # High Card

        # JOKER BONUS
        if "J" in self.counts.keys():            
            joker_count = self.counts["J"]
            if joker_count == 5:
                self.rank = 50
            elif self.rank == 22 and joker_count == 1:
                self.rank = 32
            else:
                current_index = rank_list.index(self.rank)
                new_index = current_index - joker_count
                self.rank = rank_list[new_index]
 
        self.type = self.rank
        self.rank = 0

    # custom sorting function/compare
    def __lt__(self, other):
        if self.type == other.type:
            # look at each card (we can hard code five values, no worries) and compare
            for i in range(5):
                if self.cards[i] != other.cards[i]:
                    return card_ranks.index(self.cards[i]) > card_ranks.index(other.cards[i])
            return False
        else:
            return self.type < other.type

    def winnings(self):
        return self.bid * self.rank

    def __str__(self):
        return f"{self.bid} {self.cards}"

    def __repr__(self):
        return f"{self.bid} {self.cards}"
    
    def helper_output(self):
        print("******************************")
        print("Hand: ", self.cards)
        print("Type: ", self.type)
        print("Rank: ", self.rank)

    def output_cards(self):
        print(self.cards)
        

answer = 0
hands = []

f = open("input.txt", "r")

for line in f.readlines():
    # each line contains: hand, bid
    line = line.strip()
    line = line.split(" ")
    hands.append(Hand(line[0], int(line[1])))

# magic sort
hands.sort()

# assign ranks
for i in range(len(hands)):
    hands[i].rank = i + 1

# find the answer
for hand in hands:
    answer += hand.winnings()

print(hands)
# for hand in hands:
#     print(hands)

# # output
# for hand in hands:
#     hand.helper_output()

# close the file
f.close()

print("Card Ranks: ", card_ranks)
print("Answer: ", answer)
exit()



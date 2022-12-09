#!/usr/bin/env python3
#--- Day 3: Rucksack Reorganization ---
# https://adventofcode.com/2022/day/3

# ------------- IMPORT DECLARATION --------------


# ------------- DATA DECLARATION --------------

class PuzzleData:
    """--- PuzzleData only purpose to encapsulate
       --- variables used accross the puzzle:
         * UPPERCASE: pseudo constant
         * lowercase: global vars
       -------------------------------------------
    """

    rucksacks = []

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input_file):

    i = 0
    for line in input_file:
            PuzzleData.rucksacks.append(line)

# ------------- PUZZLE METHODS --------------

def priority(itemtype):
    # A-Z
    if ord(itemtype) <= 90:
        return ord(itemtype) - 38
    # a-z
    else:
        return ord(itemtype) - 96



def rucksack_priority(compartment1, compartment2):
    for itemtype in compartment1:
        if itemtype in compartment2:
           return priority(itemtype)

def group_priority(rucksack1, rucksack2, rucksack3):
    for itemtype in rucksack1:
        if itemtype in rucksack2 and itemtype in rucksack3:
           return priority(itemtype)


# ------------- MAIN METHOD --------------

def main():

    sum_priorities_1 = 0
    sum_priorities_2 = 0

    groups = ""
    for index, rucksack in enumerate(PuzzleData.rucksacks):

        compartment1 = rucksack[0:int(len(rucksack)/2)]
        compartment2 = rucksack[int(len(rucksack)/2):]
        sum_priorities_1 = sum_priorities_1 + rucksack_priority(compartment1, compartment2)

        if index % 3 == 0:
            rucksack1 = PuzzleData.rucksacks[index]
            rucksack2 = PuzzleData.rucksacks[index + 1]
            rucksack3 = PuzzleData.rucksacks[index + 2]
            sum_priorities_2 = sum_priorities_2 + group_priority(rucksack1, rucksack2, rucksack3)
            groups = ""

    print_answers(sum_priorities_1, sum_priorities_2)


# ------------- don't touch: adventofcode --------------

def load_input_file():
    file = "input.txt" if not __debug__ else 'test.txt'
    with open(file, 'r') as reader:
        input_file = [i.rstrip("\n") for i in reader.readlines()]
    if len(input_file) == 0:
        assert False
    return input_file

# ------------- don't touch: adventofcode --------------
def print_answers(part1, part2):
    print("part 1 answer: ", part1)
    print("part 2 answer: ", part2)

# ------------- don't touch: main adventofcode --------------

if __name__ == '__main__':
    if __debug__:
        print("=== initializing data... ===", end="\n")
    init_data(load_input_file())
    if __debug__:
        print("=== solving puzzle... ===", end="\n")
    main()

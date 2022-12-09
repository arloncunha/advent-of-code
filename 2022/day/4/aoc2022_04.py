#!/usr/bin/env python3
#--- Day 4: Camp Cleanup ---
# https://adventofcode.com/2022/day/4

# ------------- IMPORT DECLARATION --------------

import re

# ------------- DATA DECLARATION --------------

class PuzzleData:
    """--- PuzzleData only purpose to encapsulate
       --- variables used accross the puzzle:
         * UPPERCASE: pseudo constant
         * lowercase: global vars
       -------------------------------------------
    """
    pair_sections = []


# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input_file):

    index = 0
    for line in input_file:
            m = re.search(r"(.+)-(.+),(.+)-(.+)", line)
            PuzzleData.pair_sections.append([])
            PuzzleData.pair_sections[index].append(int(m.group(1)))
            PuzzleData.pair_sections[index].append(int(m.group(2)))
            PuzzleData.pair_sections[index].append(int(m.group(3)))
            PuzzleData.pair_sections[index].append(int(m.group(4)))
            index = index + 1

# ------------- PUZZLE METHODS --------------

def does_fully_contain(section_1, section_2, section_3, section_4):

    if section_1 <= section_3 and section_2 >= section_4:
        return True
    if section_3 <= section_1 and section_4 >= section_2:
        return True
    return False

def overlap_pairs(section_1, section_2, section_3, section_4):

    if section_1 <= section_3 and section_2 >= section_3:
        return True
    if section_3 <= section_1 and section_4 >= section_1:
        return True
    return False


# ------------- MAIN METHOD --------------

def main():

    fully_contains1 = 0
    overlap_pairs2 = 0
    for pairs in PuzzleData.pair_sections:
        fully_contains1 = fully_contains1 + does_fully_contain(pairs[0],pairs[1],pairs[2],pairs[3])
        overlap_pairs2 = overlap_pairs2 + overlap_pairs(pairs[0],pairs[1],pairs[2],pairs[3])

    print_answers(fully_contains1, overlap_pairs2)


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

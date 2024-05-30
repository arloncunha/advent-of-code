#!/usr/bin/env python3
#--- Day 1: Calorie Counting ---
# https://adventofcode.com/2022/day/1

# ------------- IMPORT DECLARATION --------------


# ------------- DATA DECLARATION --------------

class PuzzleData:
    """--- PuzzleData only purpose to encapsulate
       --- variables used accross the puzzle:
         * UPPERCASE: pseudo constant
         * lowercase: global vars
       -------------------------------------------
    """

    elfs_calories: list = []

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input_file):
    i = 0
    PuzzleData.elfs_calories.append([])
    for row in input_file:
        if row == "":
            i = i + 1
            PuzzleData.elfs_calories.append([])
        else:
            PuzzleData.elfs_calories[i].append(int(row))

# ------------- PUZZLE METHODS --------------


# ------------- MAIN METHOD --------------

def main():


    sum_elfs_calories = (list(map(lambda x: sum(x), PuzzleData.elfs_calories)))
    sum_elfs_calories = sorted(sum_elfs_calories, reverse=True)

    part1 = sum_elfs_calories[0]
    part2 = sum_elfs_calories[0] +  sum_elfs_calories[1] +  sum_elfs_calories[2]

    print_answers(part1, part2)


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

#!/usr/bin/env python3
# Copyright (c) 2024, https://github.com/arloncunha

# --- Day 1: Historian Hysteria ---
# https://adventofcode.com/2024/day/1

# ------------- IMPORT DECLARATION --------------

import sys
sys.path.extend(['.', '../../../../utils/'])
import utils

# ------------- DATA DECLARATION --------------

class PuzzleData:
    """--- PuzzleData only purpose to encapsulate
       --- variables used accross the puzzle:
         * UPPERCASE: pseudo constant
         * lowercase: global vars
       -------------------------------------------
    """

    # ------------- don't touch: main adventofcode --------------
    __example__ = False
    # ------------- example_expect_answer1 needed  --------------
    # ------------- example_expect_answer2 needed  --------------
    example_expect_answer1 = 11
    example_expect_answer2 = 31

    list_1 = []
    list_2 = []

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input):
    """--- adventofcode interface
    """

    for line in input:

        m = utils.re.match(r"(\d+)(\D+)(\d+)", line)
        PuzzleData.list_1.append(int(m.group(1)))
        PuzzleData.list_2.append(int(m.group(3)))


# ------------- PUZZLE METHODS --------------


def what_is_the_total_distance_between_your_lists(list_1: list, list_2: list):
    """What is the total distance between your lists?
    """

    list_1.sort()
    list_2.sort()
 
    distance = 0
    for i,_ in enumerate(list_1):
        distance += abs(list_1[i] - list_2[i])

    return distance

def what_is_their_similarity_score(list_1, list_2):

    similarity_score = 0 
    for n in list_1:
        appears = 0
        for m in list_2:
            if m == n:
                appears += 1
        
        similarity_score += n * appears
    
    return similarity_score


# ------------- SOLUTION INTERFACE --------------


def part1():
    """--- adventofcode interface for solving part 1
    """

    list_1 = utils.streams.deepcopy(PuzzleData.list_1)
    list_2 = utils.streams.deepcopy(PuzzleData.list_2)
    return what_is_the_total_distance_between_your_lists(list_1, list_2)


def part2():
    """--- adventofcode interface for solving part 2
    """

    list_1 = utils.streams.deepcopy(PuzzleData.list_1)
    list_2 = utils.streams.deepcopy(PuzzleData.list_2)
    return what_is_their_similarity_score(list_1, list_2)
    

# ------------- don't touch: main adventofcode --------------
# ------------- MAIN METHOD ---------------------------------

def main(input_file):

    utils.visuals.clear()
    utils.log_process_stage("initializing data")
    PuzzleData.__example__ = input_file.endswith('example.txt') == True
    init_data(utils.read_input_file(input_file))

    utils.log_process_stage("begin solving the puzzle")
    utils.log_process_stage("solving part 1")
    utils.timing.start_timer()
    answer_1 = part1()

    utils.assert_answer(answer_1, PuzzleData.example_expect_answer1, PuzzleData.__example__)
    utils.timing.lap_timer()
    utils.log_process_stage("solving part 2")
    answer_2 = part2()

    utils.assert_answer(answer_2, PuzzleData.example_expect_answer2, PuzzleData.__example__)
    utils.timing.stop_timer()
    utils.log_elapse_time()
    utils.print_answers(answer_1, answer_2)

# ------------- don't touch: main adventofcode --------------

if __name__ == '__main__':

    # receives input file
    main(sys.argv[1])

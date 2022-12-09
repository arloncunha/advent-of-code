#!/usr/bin/env python3
# Copyright (c) 2024, https://github.com/arloncunha

# --- Day 6: Tuning Trouble ---
# https://adventofcode.com/2022/day/6

# ------------- IMPORT DECLARATION --------------

import sys
sys.path.extend(['.', '../../../utils/'])
import utils

import re

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
    example_expect_answer1 = 'CMZ'
    example_expect_answer2 = 'MCD'


# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input_file, example=False):
    """--- adventofcode interface
    """

    # ------------- don't touch: main adventofcode -------------- 
    PuzzleData.__example__ = example 


# ------------- PUZZLE METHODS --------------


def part1():
    """--- adventofcode interface for solving part 1
    """


def part2():
    """--- adventofcode interface for solving part 2
    """


# ------------- don't touch: main adventofcode --------------
# ------------- MAIN METHOD ---------------------------------

def main():

    utils.log_process_stage("solving part 1")
    utils.timing.start_timer()
    answer_1 = part1()
    utils.assert_answer(answer_1, PuzzleData.example_expect_answer1, PuzzleData.__example__)
    utils.timing.lap_timer()
    utils.log_process_stage("solving part 2")
    answer_2 = part2()
    utils.assert_answer(answer_2, PuzzleData.example_expect_answer2, PuzzleData.__example__)
    utils.timing.stop_timer()
    utils.logging.log(f"elapse time part 1: {str(utils.timing.elapsed_time_btw_laps(0,1))}s", show_datetime = False)
    utils.logging.log(f"elapse time part 2: {str(utils.timing.elapsed_time_btw_laps(1,2))}s", show_datetime = False)
    utils.logging.log(f"total elapse time : {str(utils.timing.elapsed_time())}s", show_datetime = False)

    utils.print_answers(answer_1, answer_2)


# ------------- don't touch: main adventofcode --------------

import sys
if __name__ == '__main__':

    utils.visuals.clear()
    utils.log_process_stage("initializing data")
    input_file = utils.read_input_file(sys.argv[1])
    init_data(input_file, example=sys.argv[1].endswith('example.txt'))
    utils.log_process_stage("begin solving the puzzle")
    main()

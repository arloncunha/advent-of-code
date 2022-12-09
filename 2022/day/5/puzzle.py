#!/usr/bin/env python3
# Copyright (c) 2024, https://github.com/arloncunha

#--- Day 5: Supply Stacks ---
# https://adventofcode.com/2022/day/5

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
    __example__ = False # ------------- don't touch: main adventofcode --------------    
    example_expect_answer1 = 'CMZ'
    example_expect_answer2 = 'MCD'

    stack_of_crates = []
    steps = []

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input_file, example=False):

    PuzzleData.__example__ = example

    # In order to do a one pass on the input file:
    # First, loading stack structure in another variable to ensure integrity of the columns.
    # Will not when it reaches the line with the column identifiers (numbers).

    number_of_stacks = 0
    input_file_stack = []

    for line in input_file:

        if number_of_stacks == 0:
            m = re.findall(r"\s+(\d+)", line)
            if m is not None and m != []:
                number_of_stacks =int(m[-1])
                continue
            else:
                input_file_stack.append(line)

        else: # let's init the movement instructions

            n = re.match(r"move\D*(\d+)\D*from\D*(\d+)\D*to\D*(\d+)", line)
            if n is not None:
                step = []
                step.append(int(n.group(1)))
                step.append(int(n.group(2)))
                step.append(int(n.group(3)))
                PuzzleData.steps.append(step)

    PuzzleData.stack_of_crates = [[] for _ in range(number_of_stacks)]
    for line in reversed(input_file_stack):

            m = re.match(r"\s*(\s\s\s)\s*|\s*\[(\w)\]\s*", line)
            if m is not None and m != []:
                for i in range(number_of_stacks):
                    create_pos = i*4+1
                    if create_pos < len(line) and line[i*4+1] != " ":
                        PuzzleData.stack_of_crates[i].append(line[i*4+1])

    if PuzzleData.__example__:
        utils.logging.log("PuzzleData.stack_of_crates:", PuzzleData.stack_of_crates)
        utils.logging.log("PuzzleData.steps:",           PuzzleData.steps)

    # assert if example input data is loaded correctly
    if PuzzleData.__example__:
        assert PuzzleData.stack_of_crates == [['Z', 'N'], ['M', 'C', 'D'], ['P']]  
        assert len(PuzzleData.steps)      == 4 

# ------------- PUZZLE METHODS --------------


def get_num_creates_taller_stack():

    num_creates_taller_stack = 0
    for stack in PuzzleData.stack_of_crates:
        if len(stack) > num_creates_taller_stack:
            num_creates_taller_stack = len(stack)
    
    return num_creates_taller_stack

def crate_mover_9000(stack_of_crates, move_crates, from_stack, to_stack):


    stack_of_crates[to_stack].extend(reversed(stack_of_crates[from_stack][-move_crates:]))
    stack_of_crates[from_stack] = stack_of_crates[from_stack][:len(stack_of_crates[from_stack]) - move_crates]

def crate_mover_9001(stack_of_crates, move_crates, from_stack, to_stack):

    stack_of_crates[to_stack].extend(stack_of_crates[from_stack][-move_crates:])
    stack_of_crates[from_stack] = stack_of_crates[from_stack][:len(stack_of_crates[from_stack]) - move_crates]

def part1():
    """--- adventofcode interface
    """

    stack_of_crates = utils.streams.list_copy(PuzzleData.stack_of_crates)
    # in_move_crates = PuzzleData.steps[0][0]
    # in_from        = PuzzleData.steps[0][1] - 1
    # in_to          = PuzzleData.steps[0][2] - 1
    for i, step in enumerate(PuzzleData.steps):

        crate_mover_9000(stack_of_crates, step[0], step[1] - 1, step[2] -1)
        if PuzzleData.__example__:
            utils.logging.log("step:", i + 1,  "___", "move "  + str(step[0]) + " from " + str(step[1]) + " to " + str(step[2]),  "___", "Stack_of_crates:", stack_of_crates)

    res = ''
    for stack in stack_of_crates:
        if stack != []:
            res = res + stack[len(stack) - 1]
        # else:
        #     res = res + ' '
    return res

def part2():
    """--- adventofcode interface
    """

    stack_of_crates = utils.streams.list_copy(PuzzleData.stack_of_crates)

    # in_move_crates = PuzzleData.steps[0][0]
    # in_from        = PuzzleData.steps[0][1] - 1
    # in_to          = PuzzleData.steps[0][2] - 1
    for i, step in enumerate(PuzzleData.steps):
        crate_mover_9001(stack_of_crates, step[0], step[1] - 1, step[2] -1)
        if PuzzleData.__example__:
            utils.logging.log("step:", i + 1,  "___", "move "  + str(step[0]) + " from " + str(step[1]) + " to " + str(step[2]),  "___", "Stack_of_crates:", stack_of_crates)

    res = ''
    for stack in stack_of_crates:
        if stack != []:
            res = res + stack[len(stack) - 1]
        # else:
        #     res = res + ' '
    return res


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

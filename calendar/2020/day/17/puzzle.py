#!/usr/bin/env python3
# Copyright (c) 2024, https://github.com/arloncunha

# --- Day 17: Conway Cubes ---
# https://adventofcode.com/2020/day/17

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
    example_expect_answer1 = None
    example_expect_answer2 = None

    grid = []

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input):
    """--- adventofcode interface
    """

    for line in input:
        PuzzleData.grid.append(list(line))

            
# ------------- PUZZLE METHODS --------------
def draw_grid(grid):

    for row in grid:
        print(''.join(row))            

def is_active(cube):
    return cube == '#'

def cycle(grid):

    # for i in len(grid):
    #     for j in len(grid):

    return None

def count_active_neighbors(list_of_neighbors):
    sum = 0
    for cube in list_of_neighbors:
        if is_active(cube):
            sum += 1
    return sum


def how_many_cubes_are_left_in_the_active_state(grid, state):

    draw_grid(grid)
    for cube, neighbors in utils.cell_and_neighbors_walk(grid):
        print(cube, neighbors, count_active_neighbors(neighbors))



    return None

# ------------- SOLUTION INTERFACE --------------


def part1():
    """--- adventofcode interface for solving part 1
    """

    grid = utils.streams.deepcopy(PuzzleData.grid)
    how_many_cubes_are_left_in_the_active_state(grid, 6)

def part2():
    """--- adventofcode interface for solving part 2
    """

    grid = utils.streams.deepcopy(PuzzleData.grid)
    

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

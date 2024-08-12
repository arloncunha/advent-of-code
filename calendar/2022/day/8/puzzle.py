#!/usr/bin/env python3
# Copyright (c) 2024, https://github.com/arloncunha

# --- Day 8: Treetop Tree House ---
# https://adventofcode.com/2022/day/8

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
    example_expect_answer1 = 21
    example_expect_answer2 = 8

    forrest = []

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input):
    """--- adventofcode interface
    """

    for line in input:
        PuzzleData.forrest.append(utils.number_to_digit_list(line))


def look_top(forrest, row, col):
    return utils.transpose_matrix(forrest)[col][:row]
def look_down(forrest, row, col):
    return utils.transpose_matrix(forrest)[col][row+1:]
def look_left(forrest, row, col):
    return forrest[row][:col]
def look_right(forrest, row, col):
    return forrest[row][col+1:]


def scenic_score(forrest, row, col):

    # print(f"DEBUG  {forrest[row][col]=} {row=} {col=} {forrest[row]=}")
    top   = list(reversed(look_top(forrest, row, col)))
    down  = look_down(forrest, row, col)
    left  = list(reversed(look_left(forrest, row, col)))
    right = look_right(forrest, row, col)

    # print(f"DEBUG  {top=} {left=} {right=} {down=}")

    score_top = 0
    for tree in top:
        # print(f"DEBUG  {tree=} {forrest[row][col]=}")
        if forrest[row][col] > tree:
            score_top += 1
        else:
            score_top += 1
            break
    score_down = 0
    for tree in down:
        if forrest[row][col] > tree:
            score_down += 1
        else:
            score_down += 1
            break
    score_left = 0
    for tree in left:
        if forrest[row][col] > tree:
            score_left += 1
        else:
            score_left += 1
            break
    score_right = 0
    for tree in right:
        if forrest[row][col] > tree:
            score_right += 1
        else:
            score_right += 1
            break

    score = score_top * score_down * score_left * score_right
    # print(f"DEBUG  {score_top=} {score_left=} {score_right=}  {score_down=}")
    return score

def highest_scenic_score(forrest):

    highest_score = 0

    for row in range(len(forrest)):
        for col in range(len(forrest[0])):
            score = scenic_score(forrest, row, col)
            if score > highest_score:
                highest_score = score

    return highest_score


def is_tree_visible(forrest, row, col):


    # print(f"DEBUG  {forrest[row][col]=} {row=} {col=} {forrest[row]=}")
    top   = sorted(look_top(forrest, row, col),   reverse=True)
    down  = sorted(look_down(forrest, row, col),  reverse=True)
    left  = sorted(look_left(forrest, row, col),  reverse=True)
    right = sorted(look_right(forrest, row, col), reverse=True)

    if top == [] or forrest[row][col] > top[0]:
        return True
    if down == [] or forrest[row][col] > down[0]:
        return True
    if left == [] or forrest[row][col] > left[0]:
        return True
    if right == [] or forrest[row][col] > right[0]:
        return True

    return False

    # print(f"DEBUG  {forrest[row][col]=} {row=} {col=} {forrest[row]=}")
    # left  = forrest[row][:col]
    # right = forrest[row][col+1:]
    # top  = utils.transpose_matrix(forrest)[col][:row]
    # down = utils.transpose_matrix(forrest)[col][row+1:]

    # left  = sorted(forrest[row][:col+1], reverse=True)
    # right = sorted(forrest[row][col+1:], reverse=True)
    # down  = sorted(forrest[row:][col], reverse=True)
    # top   = sorted(forrest[:row][col], reverse=True)

    # print(f"DEBUG\n {left=}\n {right=}")
    # print(f"DEBUG\n {left=}\n {right=}\n {down=}\n {top=}")


    return False


def how_many_trees_are_visible(forrest):

    sum_visibles = 0
    # pause = 0

    for row in range(len(forrest)):
        for col in range(len(forrest[0])):
            sum_visibles += is_tree_visible(forrest, row, col)

    return sum_visibles


# ------------- PUZZLE METHODS --------------



# ------------- SOLUTION INTERFACE --------------


def part1():
    """--- adventofcode interface for solving part 1
    """

    forrest = utils.streams.deepcopy(PuzzleData.forrest)
    return how_many_trees_are_visible(forrest)


def part2():
    """--- adventofcode interface for solving part 2
    """

    forrest = utils.streams.deepcopy(PuzzleData.forrest)
    return highest_scenic_score(forrest)

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

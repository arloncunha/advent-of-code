#!/usr/bin/env python3
# Copyright (c) 2024, https://github.com/arloncunha

# --- Day 2: Red-Nosed Reports ---
# https://adventofcode.com/2024/day/2

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
    example_expect_answer1 = 2
    example_expect_answer2 = 4

    reports = []

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input):
    """--- adventofcode interface
    """

    for line in input:
        PuzzleData.reports.append([int(s) for s in line.split()])
    


# ------------- PUZZLE METHODS --------------

def diff_elements_in_a_list(list_numbers):
    return [list_numbers[i+1]-list_numbers[i] for i in range(len(list_numbers)-1)] 

def list_reports_minus_one_level(report):

    l = []
    for i in range(len(report)):
        r = utils.streams.deepcopy(report)
        r.pop(i)        
        l.append(r)
    return l

def is_report_safe(report):

    diff = diff_elements_in_a_list(report)
    a = sum(abs(i) for i in diff)
    b = abs(sum(i for i in diff))
    c = max(abs(i) for i in diff)
    d = min(abs(i) for i in diff)

    if a == b and c <= 3 and d > 0:
        return True
    
    return False

def is_report_safe_with_tolerance(report):

    for report in list_reports_minus_one_level(report):
        if is_report_safe(report):
            return True
    return False


def how_many_reports_are_safe(reports):

    sum = 0
    for report in reports:
        sum += is_report_safe(report)

    return sum

def how_many_reports_are_safe_with_tolerance(reports):

    sum = 0
    for report in reports:
        sum += is_report_safe_with_tolerance(report)

    return sum


# ------------- SOLUTION INTERFACE --------------


def part1():
    """--- adventofcode interface for solving part 1
    """
    reports = utils.streams.deepcopy(PuzzleData.reports)
    return how_many_reports_are_safe(reports)

def part2():
    """--- adventofcode interface for solving part 2
    """

    reports = utils.streams.deepcopy(PuzzleData.reports)
    return how_many_reports_are_safe_with_tolerance(reports)

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

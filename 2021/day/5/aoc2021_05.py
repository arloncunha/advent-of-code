#!/usr/bin/env python3
# --- Day 5: Hydrothermal Venture ---
# https://adventofcode.com/2021/day/5

import re

# ------------- DEBUG SESSION --------------

class BackgroundColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_red(skk, end=""): print("\033[91m {}\033[00m" .format(skk), end=end)           # noqa:E704
def print_green(skk, end=""): print("\033[92m {}\033[00m" .format(skk), end=end)         # noqa:E704
def print_yellow(skk, end=""): print("\033[93m {}\033[00m" .format(skk), end=end)        # noqa:E704
def print_light_purple(skk, end=""): print("\033[94m {}\033[00m" .format(skk), end=end)  # noqa:E704
def print_purple(skk, end=""): print("\033[95m {}\033[00m" .format(skk), end=end)        # noqa:E704
def print_cyan(skk, end=""): print("\033[96m {}\033[00m" .format(skk), end=end)          # noqa:E704
def print_light_gray(skk, end=""): print("\033[97m {}\033[00m" .format(skk), end=end)    # noqa:E704
def print_black(skk, end=""): print("\033[98m {}\033[00m" .format(skk), end=end)         # noqa:E704

def debug_print(skk, end="\n"):
    if not __debug__:
        return
    print_red(skk, end)

def debug_log(skk):
    if not __debug__:
        return
    print(skk)

# ------------- DATA --------------

class PuzzleData:
    """Data Section, declares global vars used accross the puzzle
       UPPERCASE_VARIABLE: to be used as constants (not locked!)
    """
    lines:   list = []  # noqa


# ------------- DECLARATIONS --------------

def write_all_points(points: dict, a, b):
    """ there are only 3 types of lines:
        - vertical is when x1 equal x2
        - horizontal is when y1 equal y2
        - diagonal (45%) is when abs(x1 - x2) = abs(y1 - y2)

    """

    l1_x_distance = a[0] - b[0]
    l1_y_distance = a[1] - b[1]

    if l1_x_distance == 0:
        l1_steps = abs(l1_y_distance) + 1
        step_x = 0
        step_y = 1 if b[1] > a[1] else -1
    elif l1_y_distance == 0:
        l1_steps = abs(l1_x_distance) + 1
        step_y = 0
        step_x = 1 if b[0] > a[0] else -1
    else:
        l1_steps = abs(l1_x_distance) + 1
        step_x = 1 if b[0] > a[0] else -1
        step_y = 1 if b[1] > a[1] else -1

    for l_step in range(l1_steps):
        l1_x = a[0] + step_x * l_step
        l1_y = a[1] + step_y * l_step

        if points.get((l1_x, l1_y)):
            points[l1_x, l1_y] += 1
        else:
            points[l1_x, l1_y] = 1


def is_line_horizontal_or_vertical(a, b):
    return True if (a[0] == b[0] or a[1] == b[1]) else False

def init_data(input_file):

    for line in input_file:
        m = re.search(r"(\d*),(\d*)\D+(\d*),(\d*)", line)
        a = (int(m.group(1)), int(m.group(2)))
        b = (int(m.group(3)), int(m.group(4)))
        PuzzleData.lines.append((a, b))
    debug_print(PuzzleData.lines)
    print_yellow("=== init data... ===", end="\n")

# ------------- LOAD FILE --------------

def load_input_file():
    file = "input.txt" if not __debug__ else 'test.txt'
    with open(file, 'r') as reader:
        input_file = [i.rstrip("\n") for i in reader.readlines()]
    if len(input_file) == 0:
        assert False
    print_yellow("=== load file... ===", end="\n")
    return input_file


# ------------- MAIN METHOD --------------

def main():

    init_data(load_input_file())

    all_points_part1: dict = {}
    all_points_part2: dict = {}
    print_yellow("=== processing... ===", end="\n")
    for line in PuzzleData.lines:
        a, b = line[0], line[1]
        if is_line_horizontal_or_vertical(a, b):
            write_all_points(all_points_part1, a, b)
        write_all_points(all_points_part2, a, b)

    print("part1: ", sum(count > 1 for count in all_points_part1.values()))
    print("part2: ", sum(count > 1 for count in all_points_part2.values()))

# ------------- MAIN --------------

if __name__ == '__main__':
    main()

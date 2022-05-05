#!/usr/bin/env python3
# --- Day 4: Giant Squid ---
# https://adventofcode.com/2021/day/4

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

# Python program to print
# colored text and background
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

def debug_board(board_dict: dict):
    if not __debug__:
        return
    board = list(board_dict)

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if board_dict[board[x + y * GRID_SIZE]] == 'X':
                print(f"{BackgroundColors.YELLOW}{board[x + y * GRID_SIZE]:<10}{BackgroundColors.RESET}", " ", end="")
            else:
                print(f"{board[x + y * GRID_SIZE]:<10}", " ", end="")
        print()

def has_board_won(board_dict):
    """Board wins when it has at least one complete row or column of marked numbers
    """
    board = list(board_dict)

    for y in range(GRID_SIZE):
        hits_row = 0
        hits_col = 0
        for x in range(GRID_SIZE):
            hits_row = hits_row + 1 if board_dict[board[x + y * GRID_SIZE]] == 'X' else 0
            hits_col = hits_col + 1 if board_dict[board[y + x * GRID_SIZE]] == 'X' else 0
        if hits_row == 5 or hits_col == 5:
            return True
    return False


def debug_sum_of_all_unmarked_numbers(board_dict):
    """The score of the winning board can now be calculated.
       Start by finding the sum of all unmarked numbers on that board;
       Then, multiply that sum by the number that was just called when the board won.
    """

    if not __debug__:
        return

    res: int = 0
    print("debug_sum_of_all_unmarked_numbers: ", end="")
    for key, hit in board_dict.items():
        res = res + int(key) if hit != 'X' else res
        if hit == 'X':
            print_yellow(" + " + str(int(key)))
    print_yellow(" = " + str(res))
    print()
    return res

def sum_of_all_unmarked_numbers(board_dict):
    """The score of the winning board can now be calculated.
       Start by finding the sum of all unmarked numbers on that board;
       Then, multiply that sum by the number that was just called when the board won.
    """
    res: int = 0
    for key, hit in board_dict.items():
        res = res + int(key) if hit != 'X' else res
    return res


# main()
if __name__ == '__main__':
    file = "input.txt" if not __debug__ else 'test.txt'
    with open(file, 'r') as reader:
        input_file = [i.rstrip("\n") for i in reader.readlines()]

    # Data section
    GRID_SIZE: int = 5
    draw_numbers_list: list = input_file[0].split(",")
    board_dict_list: list = []

    # loading board: list of dict with list[x, y, hit] = coordinates and hit or not
    b = {}
    for line in input_file[2:]:
        row = line.split()
        if row == []:
            board_dict_list.append(b)
            b = {}
        else:
            for number in row:
                b[number] = number

    board_dict_list.append(b)


    part1 = 0
    part2 = 0
    for draw in draw_numbers_list:
        debug_print("----------------------")
        debug_print("draw: " + draw)
        i = -1
        while len(board_dict_list) > 0 and i < len(board_dict_list) - 1:
            i += 1
            board = board_dict_list[i]
            if draw in board:
                board[draw] = 'X'
                if has_board_won(board):
                    if part1 == 0:
                        part1 = sum_of_all_unmarked_numbers(board) * int(draw)
                        debug_print("part1: " + str(part1))
                    debug_board(board)
                    debug_sum_of_all_unmarked_numbers(board)
                    part2 = sum_of_all_unmarked_numbers(board) * int(draw)
                    debug_print("part2: " + str(part2))
                    del board_dict_list[i]
                    i -= 1

    print("part1:", part1)
    print("part2:", part2)

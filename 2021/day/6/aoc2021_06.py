#!/usr/bin/env python3
# --- Day 6: Lanternfish ---
# https://adventofcode.com/2021/day/6


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

def debug_print(skk):
    if not __debug__:
        return
    print_red(skk, end='\n')

def debug_log(skk):
    if not __debug__:
        return
    print(skk)

# ------------- DATA --------------

class PuzzleData:
    """Data Section, declares global vars used accross the puzzle
       UPPERCASE_VARIABLE: to be used as constants (not locked!)
    """
    lanternfish_ages:   list = []  # noqa

def init_data(input_file):

    for line in input_file:
        PuzzleData.lanternfishs = list(map(int, line.split(",")))
    debug_print(PuzzleData.lanternfishs)
    print_yellow("=== init data... ===", end="\n")



# ------------- DECLARATIONS --------------

def lanternfishs_at_day(in_lanternfishs: list, in_day: int):

    res_lanternfishs: list = list(in_lanternfishs)
    print_lanternfishs: list = []

    for day in range(in_day):
        for i in range(len(res_lanternfishs)):
            if res_lanternfishs[i] != 0:
                res_lanternfishs[i] -= 1
            else:
                res_lanternfishs[i] = 6
                res_lanternfishs.append(8)
                # print_lanternfishs.append("Fish " + str(i) + " generate new fish at day " + str(day + 1).zfill(2))

        # print(f"After {(day + 1):02d} Day: Num of fishs = {len(res_lanternfishs):02d}")
    print_lanternfishs.sort()
    for p in print_lanternfishs:
        print(p)

    return res_lanternfishs

def count_lanternfishs_at_day(in_lanternfishs: list, in_day: int):
    return len(lanternfishs_at_day(in_lanternfishs, in_day))

def lanternfish_timer_at_day(in_lanternfish_timer: int, in_after_days: int, in_created_day: int = 0):
    if in_after_days < in_created_day:
        res = -1
    else:
        # special case when new fish born (timer = 8) and first timer reset
        if in_lanternfish_timer == 8 and (in_after_days - in_created_day) < 8:
            res = (in_lanternfish_timer - (in_after_days - in_created_day)) % 9
        else:
            res = (in_lanternfish_timer - (in_after_days - in_created_day)) % 7

    # print(f"{in_lanternfish_timer=} {res=} {in_after_days=} {in_created_day=}")
    return res

def num_of_fishs(in_timer, in_after_days):

    res = in_after_days // 7
    print(f"{in_timer=} {res=} {in_after_days=}")
    return res

def list_of_days_with_new_fish(in_lanternfish_timer: int, in_after_days: int, in_created_day: int = 0):
    days_with_new_fish: list = []
    for day in range(in_after_days + 1):
        fish_timer_at_day = lanternfish_timer_at_day(in_lanternfish_timer, day, in_created_day)
        if fish_timer_at_day == 0:
            days_with_new_fish.append(day)

    return days_with_new_fish

# def rec_list_of_days_with_new_fish()

def num_lanternfishs_at_day(in_lanternfish_timer: int, in_after_days: int, in_created_day: int = 0):
    return 1 + len()



# def sum_lanternfish_at_day(in_lanternfish_timer: int, in_current_day: int, in_final_day: int):
#
#     sum = 0
#     for day in list_of_days_with_new_fish(in_lanternfish_timer, in_current_day, in_final_day):
#         sum += num_lanternfish_at_day(8, in_final_day, day)
#     return sum
#
#
# def num_lanternfish_at_day(in_lanternfish_timer: int, in_current_day: int, in_final_day: int):
#
#     print(f"{in_lanternfish_timer=} {in_current_day=} {in_final_day=}")
#     return 1 + sum_lanternfish_at_day(in_lanternfish_timer, in_current_day, in_final_day)
#
# def num_lanternfishs_at_day(in_lanternfishs: list, in_current_day: int, in_final_day: int):
#
#     sum = 0
#     for fish_timer in PuzzleData.lanternfishs:
#         sum += num_lanternfish_at_day(fish_timer, in_current_day, in_final_day)
#
#     return sum


# ------------- LOAD FILE --------------

def load_input_file():
    file = "input.txt" if not __debug__ else 'test.txt'
    with open(file, 'r') as reader:
        input_file = [i.rstrip("\n") for i in reader.readlines()]
    if len(input_file) == 0:
        assert False
    print_yellow("=== load file... ===", end="\n")
    return input_file

# ------------- TEST --------------

def main_test():
    if __debug__:
        init_data(load_input_file())

        # print("num of lanternfishs:", len(lanternfishs_at_day(PuzzleData.lanternfishs, 80)))
        #
        # sum = 0
        # for fish in PuzzleData.lanternfishs:
        #     sum += num_lanternfish_at_day(fish, 0, 80)
        #
        # print("num of lanternfishs (optimized):", sum)

        print("num of lanternfishs:", len(lanternfishs_at_day(PuzzleData.lanternfishs, 18)))

        sum = 0
        for fish in PuzzleData.lanternfishs:
            sum += num_lanternfish_at_day(fish, 0, 18)

        print("num of lanternfishs (optimized):", sum)

# ------------- MAIN METHOD --------------

def main():
    if __debug__:
        exit()
    init_data(load_input_file())


# ------------- MAIN --------------

if __name__ == '__main__':
    main_test()
    main()

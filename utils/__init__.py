# Copyright (c) 2024, https://github.com/arloncunha

import sys
import re
from . import streams 
from . import command_line
from . import logging
from . import visuals
from . import timing 
from . import puzzle

# Get fully qualified class name of an object in Python
# https://stackoverflow.com/questions/2020014/get-fully-qualified-class-name-of-an-object-in-python
def class_fullname(o):
    klass = o.__class__
    module = klass.__module__
    if module == 'builtins':
        return klass.__qualname__ # avoid outputs like 'builtins.str'
    return module + '.' + klass.__qualname__

def log_process_stage(msg):
        
        # '{:^30}'.format('align centered example')
        msg_formated = '{:<20}'.format(msg)
        prefix_decoration = "==========="
        suffix_decoration = "=" * (80 - len(msg_formated))  
        logging.log(logging.decorations.BOLD + logging.fg_colors.WHITE +
                    prefix_decoration, msg_formated, suffix_decoration, show_datetime=False)

def log_puzzle_answer(part, answer):
        logging.log(logging.decorations.BOLD + logging.fg_colors.WHITE + part + " - answer:", answer, show_datetime=False)

def print_answers(part1, part2):
    log_puzzle_answer("part 1", part1)
    log_puzzle_answer("part 2", part2)

def read_input_file(filename):
    with open(filename, 'r') as reader:
        input_file = [i.rstrip("\n") for i in reader.readlines()]
    if len(input_file) == 0:
        assert False
    if filename.endswith('example.txt'):
        logging.log(f'{logging.fg_colors.CYAN}{logging.decorations.UNDERLINE}{filename}{logging.decorations.RESET} {logging.fg_colors.CYAN}input file readed{logging.decorations.RESET}')
    return input_file

def assert_answer(answer, expected, example=False):
        if example:
            logging.log(f"asserting example: {answer=} {expected=}")
            assert answer == expected, f"Answer: |{answer}|"

def log_elapse_time():
    logging.log("elapse time part 1: "+ '{:>10}'.format(str(timing.elapsed_time_btw_laps(0,1))), show_datetime = False)
    logging.log("elapse time part 2: "+ '{:>10}'.format(str(timing.elapsed_time_btw_laps(1,2))), show_datetime = False)
    logging.log("total elapse time : "+ '{:>10}'.format(str(timing.elapsed_time())),             show_datetime = False)

def merge_lists(l1, l2):
     return [*l1, *l2]  # unpack both iterables in a list literal


def list_of_dict_keys(dict_list):
    key_list = []
    for d in dict_list:
        key_list.append(get_dict_key(d))
    
    return key_list

def get_dict_key(dict, index=0):
    """--- turns a dict into a list of keys and return key[index]
    """
     
    return list(dict.keys())[index]

def strings_to_int_list(string_list):
    """--- Converting all strings in list to integers
       --- example: ['1', '-4', '3', '-6', '7']
       ---      >>> [1, -4, 3, -6, 7]
    """

    return [int(i) for i in string_list]

def number_to_digit_list(number):
    """--- Converting integer to digit list
    """

    return [int(x) for x in str(number)]


def is_positive(num):
     return num >= 0

def transpose_matrix(m):
     # short circuits at shortest nested list if table is jagged
    return list(map(list, zip(*m)))

# def sanitized_sqrt(numbers):
#     import math
#     cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
#     return list(cleaned_iter)

# sanitized_sqrt([25, 9, 81, -16, 0])
# >>> [5.0, 3.0, 9.0, 0.0]


def matrix_walk_into_list_of_neighbors(list_of_lists, include_diagonal=True, none_for_out_range=True):
    """--- cell + list of adjacent cells, clockwise starting from top (12 o'clock)
           if ignore_out_range then list only with valid values (less neighbors) otherwise
           non-neibhbors will be None
    """ 
    # print(f"DEBUG {range(len(list_of_lists))=}")
    for row in range(len(list_of_lists)):
        for col in range(len(list_of_lists[row])):
            # print(f"DEBUG {row=}")
            # print(f"DEBUG {len(row)=}")

            l = []
            l.append(list_of_lists[row][col])
            if row > 0:             
                l.append(list_of_lists[row - 1][col]) # TOP
            elif none_for_out_range:
                 l.append(None)
            if include_diagonal and (row > 0 and col < len(list_of_lists[row]) - 1):
                l.append(list_of_lists[row - 1][col + 1]) # TOP - RIGHT
            elif include_diagonal and none_for_out_range:
                 l.append(None)
            if col < len(list_of_lists[row]) - 1:
                l.append(list_of_lists[row][col + 1]) # RIGHT
            elif none_for_out_range:
                 l.append(None)
            if include_diagonal and (row < len(list_of_lists) - 1 and col < len(list_of_lists[row]) - 1):
                l.append(list_of_lists[row + 1][col + 1]) # DOWN - RIGHT
            elif include_diagonal and none_for_out_range:
                 l.append(None)
            if (row < len(list_of_lists) - 1):
                l.append(list_of_lists[row + 1][col]) # DOWN
            elif none_for_out_range:
                 l.append(None)
            if include_diagonal and (row < len(list_of_lists) - 1 and col > 0):
                l.append(list_of_lists[row + 1][col -1]) # DOWN - LEFT
            elif include_diagonal and none_for_out_range:
                 l.append(None)
            if col > 0:
                l.append(list_of_lists[row][col - 1]) # LEFT
            elif none_for_out_range:
                 l.append(None)
            if include_diagonal and (row > 0 and col > 0):
                l.append(list_of_lists[row - 1][col - 1]) # TOP - LEFT
            elif include_diagonal and none_for_out_range:
                 l.append(None)
                 

            # print(f"DEBUG {row=}{col=} {list_of_lists[row][col]} {l=}")

            yield l


# Mapping consists of applying a transformation function to an iterable to produce a new iterable. Items in the new iterable are produced by calling the transformation function on each item in the original iterable.

# Filtering consists of applying a predicate or Boolean-valued function to an iterable to generate a new iterable. Items in the new iterable are produced by filtering out any items in the original iterable that make the predicate function return false.

# Reducing consists of applying a reduction function to an iterable to produce a single cumulative value.
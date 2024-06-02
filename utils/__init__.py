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
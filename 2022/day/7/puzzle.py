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
    example_expect_answer1 = 95437
    example_expect_answer2 = 24933642

    filesystem = {}

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input_file, example=False):
    """--- adventofcode interface
    """

    # ------------- don't touch: main adventofcode -------------- 
    PuzzleData.__example__ = example 

    # dir  = {<dirname> :  {'dir' : { dirs... }}}
    # file = {{<filename>: {'file': <file_size>}}

    # initialize roor dir
    PuzzleData.filesystem['/'] = {'dir': {}}
    # working directory
    pwd = PuzzleData.filesystem['/']['dir']
    # working directory history
    wd_hist = []
    wd_hist.append(pwd)
    # print(f"DEBUG {pwd=}")

    for line in input_file:

        # 'ls' can be just ignored

        m = re.match(r"\$\s(cd)\s(\S+)", line)
        if m is not None:
            # print(f"DEBUG cd dir {m.group(2)}")
            # print(f"DEBUG pwd dir {pwd=}")

            if m.group(2) in pwd:
                # print(f"DEBUG go to {m.group(2)}")
                wd_hist.append(pwd[m.group(2)]['dir'])
                pwd = pwd[m.group(2)]['dir']
                # print(f"DEBUG new pwd {m.group(2)}")
                # input()

            # if m.group(2) in '..' and not wd_hist:
                # print(f"DEBUG in root")
            if m.group(2) in '..' and wd_hist:
                # print(f"DEBUG in dir {m.group(2)} back ..")
                wd_hist.pop()
                # print(f"DEBUG pop dir {wd_hist=}")
                if wd_hist:
                    pwd = wd_hist[len(wd_hist)-1]
                # input()

            # if m.group(2) in '..':
            #     pwd.append({'dir': m.group(2)})

        m = re.match(r"(dir)\s(\S+)", line)
        if m is not None:
            # print(f"DEBUG ls dir {m.groups()}")
            if m.group(2) not in pwd:
                # print(f"DEBUG ls dir {m.group(2)=}")
                # input()
                pwd[m.group(2)] = {'dir': {}}


        m = re.match(r"(\d+)\s(\S+)", line)
        if m is not None:
            # print(f"DEBUG ls file {m.groups()} {m.group(0)=} {int(m.group(1))=}  {m.group(2)=}")
            if m.group(2) not in pwd:
                pwd[m.group(2)] = {}
                pwd[m.group(2)]['file'] =  ''
                pwd[m.group(2)]['size'] = int(m.group(1))

    if PuzzleData.__example__:
        utils.logging.log(f"{PuzzleData.filesystem=}")
        from pprint import pprint
        pprint(PuzzleData.filesystem)

# ------------- PUZZLE METHODS --------------

def dir_size(dir):

    size = 0
    for item in dir['dir'].items():
        # print(f"DEBUG size\n{item=}\n{item[0]=}\n{item[1]=}\n")
        # print(f"DEBUG {item=}")
        if 'dir' in item[1]:
            # print(f"DEBUG {item[1]['dir']=}")
            size += dir_size(item[1])
        else:
            # print(f"DEBUG {item[1]['size']=}")
            size += item[1]['size']

    return size

def sum_size_if_at_most_100000(dir):
    total_size = 0
    for item in dir['dir'].items():
        if 'dir' in item[1]:
            size = dir_size(item[1])
            # print(f"{size=} DEBUG {item[0]=}")
            total_size += size if size < 100000 else 0
            total_size += sum_size_if_at_most_100000(item[1])
    return total_size


def smallest_dir_to_delete(dirname, dir):

    total_disk_space    = 70000000
    unused_space_needed = 30000000

    dir_list = dir_size_list(dirname, dir)

    # print(f"DEBUG {dir_list=}")
    # print(f"DEBUG {list(reversed(dir_list))=}")

    total_used_space = int(utils.get_dict_key(list(reversed(dir_list))[0], 0)) 

    # print(f"DEBUG {dir_list=}")


    for dir in dir_list:
        # print(f"DEBUG {dir=}")
        # print(f"DEBUG {dir=} {list(dir.keys())[0]=}")
        dir_size = int(utils.get_dict_key(dir, 0))
        # print(f"DEBUG {dir_size=}")
        
        if (total_used_space - dir_size) <= unused_space_needed:
            return dir_size
    return 0


def dir_size_list(dirname, dir):
    dirs = []
    total_size = 0
    for item in dir['dir'].items():
        if 'dir' in item[1]:
            # size = dir_size(item[1])
            # dirs.append({str(size): item[0]})
            # print(f"{size=} DEBUG {item[0]=}")
            # total_size += size
            # print(f"DEBUG merge {item[0]=} {size=}")
            dirs = utils.merge_lists(dirs, (dir_size_list(item[0], item[1])))
            # print(f"DEBUG merge {dirs=}")
    # print(f"DEBUG totalsize {total_size=} {dirname=}")
    dirs.append({str(dir_size(dir)): dirname})
    return dirs
    return total_size



def part1():
    """--- adventofcode interface for solving part 1
    """

    filesystem = utils.streams.deepcopy(PuzzleData.filesystem)
    # print(f"DEBUG {dir_size(filesystem['/']['dir'])}=")
    # print(f"DEBUG {dir_size(filesystem['/']['dir']['a']['dir']['e']['dir'])}=")
    # print(f"DEBUG {dir_size(filesystem['/']['dir']['a']['dir'])}=")

    return sum_size_if_at_most_100000(filesystem['/'])

def part2():
    """--- adventofcode interface for solving part 2
    """
    filesystem = utils.streams.deepcopy(PuzzleData.filesystem)
    # print(f"DEBUG {filesystem['/']=}")
    # print(f"DEBUG {dir_size_list('/', filesystem['/'])}")
    return smallest_dir_to_delete('/', filesystem['/'])


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
    utils.log_elapse_time()
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

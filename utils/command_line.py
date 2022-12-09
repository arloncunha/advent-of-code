# Copyright (c) 2024, https://github.com/arloncunha

import argparse

def load_cmd_line_args():
    parser = argparse.ArgumentParser(
                        prog        ='Advent of Code',
                        description ='Collection of programs to solve Advent of Code',
                        epilog      ='Copyright (c) 2023, Arlon Cunha <arloncunha@dotarlon.com>')

    parser.add_argument('-y', '--year',    type=int)
    parser.add_argument('-d', '--day',     type=int)
    parser.add_argument('-e', '--example', action='store_true')  # on/off flag
    parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
    args = parser.parse_args()
    return args

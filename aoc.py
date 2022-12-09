#!/usr/bin/env python3
# Copyright (c) 2024, https://github.com/arloncunha

import os
import utils.command_line as command


# -- Main  -------------------------------------------------------------------------------------------------

def main():

    cmd_line_args = command.load_cmd_line_args()
    YEAR        = cmd_line_args.year
    DAY         = cmd_line_args.day
    EXAMPLE     = cmd_line_args.example
    INPUT_FILE  = 'example.txt' if EXAMPLE else 'input.txt'
    
    os.system(f'python ./{YEAR}/day/{DAY}/puzzle.py ./{YEAR}/day/{DAY}/{INPUT_FILE}')

# -- Execute -------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

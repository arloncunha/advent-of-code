# Copyright (c) 2024, https://github.com/arloncunha

from . import logging 
import copy

# https://docs.python.org/3/library/io.html

def read_file(filename):

    with open(filename) as f:
        contents = f.read()
    return contents

def save_file(content, filename):

    import os
    filename = '../output/' + os.path.basename(filename)
    with open(filename, "w") as f:
        f.write(content)
    logging.log(f'{logging.decorations.UNDERLINE}{filename}{logging.decorations.RESET} saved')


def list_copy(from_list):
    return copy.deepcopy(from_list)

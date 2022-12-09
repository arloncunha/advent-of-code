# Copyright (c) 2024, https://github.com/arloncunha

import curses
import os

def curses_clear():

    SCREEN = curses.initscr()
    SCREEN.clear()
    SCREEN.refresh()
    # curses.nocbreak()
    # curses.echo()
    curses.endwin()
    
def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')



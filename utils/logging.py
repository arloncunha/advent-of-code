# Copyright (c) 2024, https://github.com/arloncunha

# TODO improve debug toggle
DEBUG = False 

    # https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# https://en.wikipedia.org/wiki/ANSI_escape_code
class fg_colors:
    BLACK   = '\033[0;30m'
    RED     = '\033[0;31m'
    GREEN   = '\033[0;32m'
    YELLOW  = '\033[0;33m'
    BLUE    = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN    = '\033[0;36m'
    WHITE   = '\033[0;37m'
    DEFAULT = '\033[0;39m'    # Default foreground color Implementation defined (according to standard)

class bg_colors:
    BLACK   = '\033[0;40m'
    RED     = '\033[0;41m'
    GREEN   = '\033[0;42m'
    YELLOW  = '\033[0;43m'
    BLUE    = '\033[0;44m'
    MAGENTA = '\033[0;45m'
    CYAN    = '\033[0;46m'
    WHITE   = '\033[0;47m'
    DEFAULT = '\033[0;49m'    # Default background color Implementation defined (according to standard)

class decorations:
    BOLD        = '\033[0;1m'
    FAINT       = '\033[0;2m'   # decreased intensity, or dim
    ITALIC      = '\033[0;3m'   # not widely supported, sometimes treated as inverse or blink
    UNDERLINE   = '\033[0;4m'
    REVERSE     = '\033[0;7m'   
    RESET       = '\033[0m'

class control_sequences:
    # Moves the cursor n (default 1) cells in the given direction.
    # If the cursor is already at the edge of the screen, this has no effect.
    UP            = '\033[A'
    DOWN          = '\033[B'
    RIGHT         = '\033[C'
    LEFT          = '\033[D'
    # Moving cursor to the edge (n = 9999 as arbiratry large number of cells)
    UP_EDGE       = '\033[9999A'  
    DOWN_EDGE     = '\033[9999B'
    RIGHT_EDGE    = '\033[9999C'
    LEFT_EDGE     = '\033[9999D'
    # Erases part of the line:
    #  If n is 0 (or missing), clear from cursor to the end of the line. 
    #  If n is 1, clear from cursor to beginning of the line. 
    #  If n is 2, clear entire line. Cursor position does not change.
    ERASE_RIGHT   = '\033[0K'
    ERASE_LEFT    = '\033[1K'
    ERASE_LINE    = '\033[2K'

#  Using log($args) combined with " ".join(map(str,args)) so print() can handle multiple args

def log(*args, show_datetime=True, end="\n"):
    import datetime
    log_datetime = bg_colors.CYAN + str(datetime.datetime.now())  + decorations.RESET + " " if show_datetime else "" 
    print(log_datetime + fg_colors.CYAN + " ".join(map(str,args)) + decorations.RESET, end=end)

def debug(*args, ignore_debug_mode = False):
    import datetime
    if DEBUG or ignore_debug_mode:
        print(decorations.ITALIC, bg_colors.RED, datetime.datetime.now(), decorations.RESET, fg_colors.RED, " ".join(map(str,args)), decorations.RESET)
        input()

def loading():
    import time, sys
    print =("Loading...")
    for i in range(0, 100):        
        time.sleep(0.1)
        sys.stdout.write(u"\033[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
        
def loading_bar():
    import time, sys
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        width = (i + 1) / 4
        bar = "[" + "#" * int(width) + " " * int(25 - width) + "]"
        sys.stdout.write(u"\033[1000D" +  bar)
        sys.stdout.flush()
    print

def test_loading_bar(count):
    import time, sys, random
    all_progress = [0] * count
    sys.stdout.write("\n" * count) # Make sure we have space to draw the bars
    while any(x < 100 for x in all_progress):
        time.sleep(0.01)
        # Randomly increment one of our progress values
        unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < 100]
        index, _ = random.choice(unfinished)
        all_progress[index] += 1
        
        # Draw the progress bars
        sys.stdout.write(u"\033[1000D") # Move left
        sys.stdout.write(u"\033[" + str(count) + "A") # Move up
        for progress in all_progress: 
            width = progress / 4
            print("[" + "#" * width + " " * (25 - width) + "]")

 
def test_command_line():
    import sys, tty
    tty.setraw(sys.stdin)
    while True: # loop for each line
    # Define data-model for an input-string with a cursor
        input = ""
        index = 0
        while True: # loop for each character
            char = ord(sys.stdin.read(1)) # read one char and get char code
            
            # Manage internal data-model
            if char == 3: # CTRL-C
                return
            elif 32 <= char <= 126:
                input = input[:index] + chr(char) + input[index:]
                index += 1
            elif char in {10, 13}:
                sys.stdout.write(u"\033[1000D")
                print("\nechoing... ", input)
                input = ""
                index = 0
            elif char == 27:
                next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                if next1 == 91:
                    if next2 == 68: # Left
                        index = max(0, index - 1)
                    elif next2 == 67: # Right
                        index = min(len(input), index + 1)
            elif char == 127:
                input = input[:index-1] + input[index:]
                index -= 1
            # Print current input-string
            sys.stdout.write(u"\033[1000D") # Move all the way left
            sys.stdout.write(u"\033[0K")    # Clear the line
            sys.stdout.write(input)
            sys.stdout.write(u"\033[1000D") # Move all the way left again
            if index > 0:
                sys.stdout.write(u"\033[" + str(index) + "C") # Move cursor too index
            sys.stdout.flush()
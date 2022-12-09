#!/usr/bin/env python3
#--- Day 2: Rock Paper Scissors ---
# https://adventofcode.com/2022/day/2

# ------------- IMPORT DECLARATION --------------

import re


# ------------- DATA DECLARATION --------------

class PuzzleData:
    """--- PuzzleData only purpose to encapsulate
       --- variables used accross the puzzle:
         * UPPERCASE: pseudo constant
         * lowercase: global vars
       -------------------------------------------
    """

    GAME_SHAPE = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
}

    ROUND_ENDS = {
        "X": "lost",
        "Y": "draw",
        "Z": "won"
}

#     GAME_SCORE = {
#         "rock": 1,
#         "paper": 2,
#         "scissors": 3,
#         "lost": 0,
#         "draw": 3,
#         "won": 6
# }

    rounds = []

# ------------- INITIALIZE PUZZLE DATA METHOD  --------------

def init_data(input_file):

    i = 0
    for line in input_file:
            PuzzleData.rounds.append([])
            m = re.search(r"(.) (.)", line)
            PuzzleData.rounds[i].append(m.group(1))
            PuzzleData.rounds[i].append(m.group(2))
            i = i + 1

# ------------- PUZZLE METHODS --------------

def round_score1(opponent, me):

    # return shape + outcome of the round score
    if opponent == "rock"     and me == "rock"     : return 1 + 3 # "draw"
    if opponent == "rock"     and me == "paper"    : return 2 + 6 # "won"
    if opponent == "rock"     and me == "scissors" : return 3 + 0 # "lost"
    if opponent == "paper"    and me == "rock"     : return 1 + 0 # "lost"
    if opponent == "paper"    and me == "paper"    : return 2 + 3 # "draw"
    if opponent == "paper"    and me == "scissors" : return 3 + 6 # "won"
    if opponent == "scissors" and me == "rock"     : return 1 + 6 # "won"
    if opponent == "scissors" and me == "paper"    : return 2 + 0 # "lost"
    if opponent == "scissors" and me == "scissors" : return 3 + 3 # "draw"

def round_score2(opponent, me):

    # return outcome of the round + shape score
    if opponent == "rock"     and me == "draw" : return 1 + 3 # "rock"
    if opponent == "rock"     and me == "won"  : return 2 + 6 # "paper"
    if opponent == "rock"     and me == "lost" : return 3 + 0 # "scissors"
    if opponent == "paper"    and me == "draw" : return 2 + 3 # "paper"
    if opponent == "paper"    and me == "won"  : return 3 + 6 # "scissors"
    if opponent == "paper"    and me == "lost" : return 1 + 0 # "rock"
    if opponent == "scissors" and me == "draw" : return 3 + 3 # "scissors"
    if opponent == "scissors" and me == "won"  : return 1 + 6 # "paper"
    if opponent == "scissors" and me == "lost" : return 2 + 0 # "scissors"

# ------------- MAIN METHOD --------------

def main():

    score_round1 = 0
    score_round2 = 0
    for round in PuzzleData.rounds:
        score_round1 = score_round1 + round_score1(PuzzleData.GAME_SHAPE[round[0]], PuzzleData.GAME_SHAPE[round[1]])
        score_round2 = score_round2 + round_score2(PuzzleData.GAME_SHAPE[round[0]], PuzzleData.ROUND_ENDS[round[1]])

    print_answers(score_round1, score_round2)


# ------------- don't touch: adventofcode --------------

def load_input_file():
    file = "input.txt" if not __debug__ else 'test.txt'
    with open(file, 'r') as reader:
        input_file = [i.rstrip("\n") for i in reader.readlines()]
    if len(input_file) == 0:
        assert False
    return input_file

# ------------- don't touch: adventofcode --------------
def print_answers(part1, part2):
    print("part 1 answer: ", part1)
    print("part 2 answer: ", part2)

# ------------- don't touch: main adventofcode --------------

if __name__ == '__main__':
    if __debug__:
        print("=== initializing data... ===", end="\n")
    init_data(load_input_file())
    if __debug__:
        print("=== solving puzzle... ===", end="\n")
    main()

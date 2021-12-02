# --- Day 15: Rambunctious Recitation ---
# https://adventofcode.com/2020/day/15

#remarks
# - speak either 0 (if the last number is new) or an age (if the last number is a repeat)
# - part1 worked with list, part2 due to efficiency needed to learn/change to dict
# - part1 and part2 timing: 5.248828 secs

# def part1_number_spoken(number_list, last_turn):
#
#     turn_list = [i for i in range(1, len(number_list)+1)]
#     spoke = 0
#     aux_spoke = 0
#     for turn in range(len(number_list) + 1, last_turn):
#         if spoke in number_list:
#             aux_spoke = spoke
#             idx = number_list.index(spoke)
#             spoke = turn - turn_list[idx]
#             turn_list[idx] = turn
#         else:
#             number_list.append(spoke)
#             turn_list.append(turn)
#             spoke = 0
#     return spoke

def number_spoken(init_list, last_turn):

    spoken_dict = {init_list[i]:i+1 for i in range(len(init_list))}
    spoke = 0
    for turn in range(len(init_list) + 1, last_turn):
            spoken_dict[spoke], spoke = turn, turn - spoken_dict[spoke] if spoke in spoken_dict else 0
    return spoke

input = [7,12, 1, 0,16, 2]
print(number_spoken(input, 2020))
print(number_spoken(input, 30000000))

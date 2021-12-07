# --- Day 4: Giant Squid ---
# https://adventofcode.com/2021/day/4

def score(board_dict):
    hits = 0
    res = 0
    board = list(board_dict)

    for y in range(GRID_SIZE):
        hits_row = 0
        hits_col = 0
        for x in range(GRID_SIZE):
            # print(board_dict[board[x + y]], board[x + y], x, y)
            hits_row = hits_row + 1 if board_dict[board[x + y * GRID_SIZE]] == 'X' else 0
            hits_col = hits_col + 1 if board_dict[board[y + x * GRID_SIZE]] == 'X' else 0

        if hits_row == 5:
            for z in range(GRID_SIZE):
                board_dict[board[z + y * GRID_SIZE]] = 'W'
            for i in range(len(board)):
                res = res + int(board[i]) if board_dict[board[i]] != 'W' and board_dict[board[i]] != 'X' else res
            return res
        if hits_col == 5:
            for z in range(GRID_SIZE):
                board_dict[board[y + z * GRID_SIZE]] = 'W'
            for i in range(len(board)):
                res = res + int(board[i]) if board_dict[board[i]] != 'W' and board_dict[board[i]] != 'X' else res
            return res

    return 0

with open('test.txt', 'r') as reader:
    input_file = [i.rstrip("\n") for i in reader.readlines()]

# data
GRID_SIZE = 5
draw_numbers_list = input_file[0].split(",")
board_list_dict = []

# loading board: list of dict with list[x, y, hit] = coordinates and hit or not
b = {}
for line in input_file[2:]:
    row = line.split()
    if row == []:
        board_list_dict.append(b)
        b = {}
    else:
        for number in row:
            b[number] = None
board_list_dict.append(b)

for draw in draw_numbers_list:

    print("draw :", int(draw))
    for idx, board in enumerate(board_list_dict):
        if draw in board:
            board[draw] = 'X'
            part1 = score(board)
            if part1 > 0:
                print(part1 * int(draw))
                break
    if part1 > 0:
        break




    # print(board_list_dict)
    # input()


# line = input_file[i].split(" ")
